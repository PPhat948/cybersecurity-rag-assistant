import os
import json
from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnablePassthrough
from app.models import AnswerWithCitation

# Configuration
INDEX_PATH = "./faiss_index"
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL_NAME = "llama3.1:8b"

import torch

# Global instances for caching
_llm_instance = None
_retriever_instance = None

def get_llm():
    """
    Initialize the ChatOllama model (cached).
    - temperature=0: Ensures deterministic outputs, crucial for factual RAG.
    - format="json": Forces Llama 3 to output valid JSON, reducing parsing errors.
    """
    global _llm_instance
    if _llm_instance is None:
        print("Initializing LLM...")
        _llm_instance = ChatOllama(
            base_url=OLLAMA_BASE_URL,
            model=MODEL_NAME,
            temperature=0,
            format="json",
            keep_alive=-1  # Keep the model loaded indefinitely
        )
    return _llm_instance

def get_retriever():
    """
    Load the FAISS index and return a retriever (cached).
    """
    global _retriever_instance
    if _retriever_instance is None:
        if not os.path.exists(INDEX_PATH):
            raise FileNotFoundError(f"FAISS index not found at {INDEX_PATH}. Please run ingestion first.")
        
        print(f"Loading embeddings model: {EMBEDDING_MODEL_NAME}...")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_kwargs = {'device': device}
        encode_kwargs = {'normalize_embeddings': True}
        
        embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL_NAME,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        
        # allow_dangerous_deserialization is needed because pickle is used by FAISS
        print(f"Loading FAISS index from {INDEX_PATH}...")
        vectorstore = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
        
        # k=4: Retrieve top 4 most relevant chunks to balance context window and precision
        _retriever_instance = vectorstore.as_retriever(search_kwargs={"k": 4})
        
    return _retriever_instance

def format_docs(docs):
    """
    Format retrieved documents into a string for the prompt.
    Also logs retrieved sources for debugging.
    """
    print(f"\n--- DEBUG: Retrieved {len(docs)} chunks ---")
    for i, doc in enumerate(docs):
        print(f"[Chunk {i+1} | Source: {doc.metadata.get('source', 'unknown')}]")
        print(f"Content: {doc.page_content[:200]}...") # Log first 200 chars to check for decoding errors
        print("-" * 50)
    
    formatted = []
    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        content = doc.page_content.replace("\n", " ")
        formatted.append(f"Source: {source}\nContent: {content}")
    return "\n\n".join(formatted)

def generate_answer(question: str) -> AnswerWithCitation:
    """
    Core RAG function.
    1. Retrieve context.
    2. Prompt LLM to answer in JSON with citations.
    3. Parse and return.
    """
    # Get cached instances
    llm = get_llm()
    retriever = get_retriever()
    parser = JsonOutputParser(pydantic_object=AnswerWithCitation)

    # Strict System Prompt
    # We explicitly instruct the model to use ONLY the context and format as JSON.
    template = """
    You are a cybersecurity expert assistant. Answer the user's question properly.
    
    Instructions:
    1. Answer ONLY using the provided context. If the answer is not in the context, say "I don't know".
    2. You MUST cite your sources. Every claim should be backed by a source from the context.
    3. Format your response strictly as a JSON object with the following keys:
       - "answer": The string answer to the question.
       - "sources": A list of strings, where each string is a filename from the "Source:" field in the context.
    
    Context:
    {context}
    
    Question: 
    {question}
    
    JSON Response:
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"],
    )

    # Build the chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | parser
    )

    try:
        response = rag_chain.invoke(question)
        return response
    except Exception as e:
        print(f"RAG Error: {e}")
        # Fallback response to avoid crashing the API
        return AnswerWithCitation(
            answer="I encountered an error while processing your request.",
            sources=[]
        )
