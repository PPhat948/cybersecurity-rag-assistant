import os
import sys
from typing import List
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Configuration
DATASET_PATH = "./dataset"
INDEX_PATH = "./faiss_index"
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"

# --- Typhoon OCR Integration ---
import fitz  # PyMuPDF
from PIL import Image
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor

def resize_if_needed(img, max_size):
    width, height = img.size
    # Only resize if one dimension exceeds max_size (logic from snippet)
    if width > 300 or height > 300:
        if width >= height:
            scale = max_size / float(width)
            new_size = (max_size, int(height * scale))
        else:
            scale = max_size / float(height)
            new_size = (int(width * scale), max_size)

        img = img.resize(new_size, Image.Resampling.LANCZOS)
        print(f"Resized image: {width, height} ==> {img.size}") 
        return img
    else:
        return img

class TyphoonOCRLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.model_id = "scb10x/typhoon-ocr1.5-2b"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Initializing Typhoon OCR on {self.device}...")
        
        # Load Model & Processor
        # Use dtype="auto" and device_map="auto" as recommended
        self.model = AutoModelForImageTextToText.from_pretrained(
            self.model_id, 
            dtype="auto",
            device_map="auto",
            trust_remote_code=True
        )
        self.processor = AutoProcessor.from_pretrained(self.model_id, trust_remote_code=True)

    def load(self) -> List[Document]:
        doc = fitz.open(self.file_path)
        full_text = ""
        
        for page_num, page in enumerate(doc):
            print(f"  - OCR Page {page_num + 1}/{len(doc)}")
            # Render page to image
            pix = page.get_pixmap(dpi=200) 
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Resize to max 1800px (model constraint)
            img = resize_if_needed(img, 1800)
            
            # OCR Inference
            try:
                prompt = "ocr this to markdown"
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "image", "image": img},
                            {"type": "text", "text": prompt}
                        ],
                    }
                ]
                
                inputs = self.processor.apply_chat_template(
                    messages,
                    tokenize=True,
                    add_generation_prompt=True,
                    return_dict=True,
                    return_tensors="pt"
                )
                inputs = inputs.to(self.model.device)
                
                # Generate
                generated_ids = self.model.generate(**inputs, max_new_tokens=4096) # Adjusted max tokens reasonable for page
                
                # Decode
                generated_ids_trimmed = [
                    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
                ]
                output_text = self.processor.batch_decode(
                    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
                )
                
                response = output_text[0]
                full_text += response + "\n\n"
                
            except Exception as e:
                print(f"    Error on page {page_num+1}: {e}")
                full_text += f"[OCR Error Page {page_num+1}]\n"

        return [Document(page_content=full_text, metadata={"source": self.file_path})]


def load_documents(path: str) -> List[Document]:
    """
    Load .md and .pdf files.
    PDFs are processed using Typhoon OCR 1.5.
    Results of OCR are saved as .md files to speed up future runs.
    """
    documents = []
    
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        return []

    # 1. Load Existing Markdown files (including previously OCR'd ones)
    print("Loading Markdown files...")
    md_loader = DirectoryLoader(path, glob="**/*.md", loader_cls=TextLoader)
    documents.extend(md_loader.load())

    # 2. Process PDF files (Only if no corresponding OCR text file exists)
    print("Checking PDF files for missing OCR...")
    pdf_files = [os.path.join(r, file) for r, d, f in os.walk(path) for file in f if file.endswith(".pdf")]
    
    for pdf_file in pdf_files:
        # Define the cache filename: e.g., document.pdf -> document_ocr.md
        ocr_filename = pdf_file.replace(".pdf", "_ocr.md")
        
        if os.path.exists(ocr_filename):
            print(f"Skipping PDF (OCR Cache found): {os.path.basename(pdf_file)}")
            continue # Already loaded in step 1
        
        print(f"Running Typhoon OCR for: {os.path.basename(pdf_file)}")
        try:
            loader = TyphoonOCRLoader(pdf_file)
            docs = loader.load()
            
            # Save the result to a markdown file
            if docs and docs[0].page_content.strip():
                print(f"Saving OCR result to: {os.path.basename(ocr_filename)}")
                with open(ocr_filename, "w", encoding="utf-8") as f:
                    f.write(docs[0].page_content)
                
                # Add to current documents list
                new_doc_loader = TextLoader(ocr_filename)
                documents.extend(new_doc_loader.load())
            
            # Clean up GPU memory
            del loader
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                
        except Exception as e:
            print(f"Failed to process {pdf_file}: {e}")

    # Ensure source metadata is strictly the filename
    for doc in documents:
        if 'source' in doc.metadata:
            doc.metadata['source'] = os.path.basename(doc.metadata['source'])
            
    print(f"Loaded {len(documents)} documents.")
    return documents

def build_index():
    print("Starting ingestion process...")
    
    # 1. Load Documents
    raw_docs = load_documents(DATASET_PATH)
    if not raw_docs:
        print("No documents found to ingest. Exiting.")
        return

    # 2. Split Text
    print("Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(raw_docs)
    print(f"Created {len(chunks)} chunks.")

    # 3. Create Embeddings
    print(f"Initializing embeddings ({EMBEDDING_MODEL_NAME})...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

    # 4. Create FAISS Vector Store
    print("Building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 5. Save Locally
    print(f"Saving index to {INDEX_PATH}...")
    vectorstore.save_local(INDEX_PATH)
    
    print("Ingestion complete!")

if __name__ == "__main__":
    build_index()
