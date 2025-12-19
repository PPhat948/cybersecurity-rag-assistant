# System Architecture

## Overview
The Cybersecurity RAG Assistant is designed as a standalone, containerized application that leverages offline Large Language Models (LLMs) and Vision-Language Models (VLMs) to answer domain-specific queries with high accuracy and strict grounding.

## System Diagram

<img width="1669" height="1348" alt="system_diagram" src="https://github.com/user-attachments/assets/f6f2807d-a221-4be1-b7bf-e34d4a79af4c" />

## Pipeline Details

The system operates entirely within a **Docker Environment**, ensuring consistent performance and isolation.

### 1. Ingestion Pipeline
The ingestion process transforms raw documents into a searchable vector index.

1.  **Raw Document**: Users place **PDF** or Markdown files in the `dataset/` folder.
2.  **OCR Model (TyphoonOCR1.5)**: PDF files are processed visually by the Typhoon 1.5 Vision-Language Model to extract text and structure into **Markdown**.
3.  **Chunking**: The Markdown text is split into smaller **Text Chunks** using a **Langchain Text Splitter** (RecursiveCharacterTextSplitter) to ensure optimal context window usage.
4.  **Document Embedding Model (BGE-M3)**: Each chunk is converted into a high-dimensional **Vector**.
5.  **Vector Database (Faiss)**: Vectors are stored and indexed in a local Faiss index for efficient retrieval.

### 2. Retrieval & Generation Pipeline
The RAG pipeline handles user queries and generates grounded answers.

1.  **User Question**: The **User** submits a question through the interface (CLI or Web).
2.  **API Service (FastAPI)**: The application receives the request and orchestrates the flow.
3.  **Embedding Query**: The question is passed to the **Embedding Model (BGE-M3)** to create a query vector.
4.  **Retriever**: The system searches the **Vector Database (Faiss)** for the **Top K Chunks** most similar to the query.
5.  **Prompt Template**: The retrieved chunks are combined with the user question into a **Final Prompt** that enforces strict grounding rules.
6.  **LLM (Llama3.1-8B)**: The model processes the prompt and generates a **Final Answer** with citations.
7.  **Response**: The answer is returned to the User via the API.

## Infrastructure & Optimization

### Containerization
*   **Base Image:** `python:3.10-slim`
*   **Dependency Management:** `uv` is used for extremely fast package resolution and installation.
*   **Service Orchestration:** `docker-compose` manages the application container and volumes.

### Hardware Acceleration
*   **GPU Support:** The container is configured via NVIDIA Container Toolkit to pass through host GPU resources.
*   **Usage:**
    *   **Ollama:** Offloads Llama 3.1 inference layers to VRAM.
    *   **Ingestion:** Uses CUDA for accelerated Typhoon OCR inference and PyTorch operations.

### Persistent Caching Strategy
To minimize bandwidth usage and startup time, the following components are cached on the host filesystem:
1.  **HuggingFace Cache (`./hf_cache`):** Stores the `BAAI/bge-m3` embedding model and `typhoon-ocr` model artifacts.
2.  **Ollama Cache (`./ollama_cache`):** Stores the `llama3.1:8b` model blobs.

## Reliability & Limitations
*   **Hallucination Control:** High temperature settings are avoided (`temperature=0`), and the system prompt explicitly penalizes external knowledge usage.
*   **Performance:**
    *   **Inference:** Dependent on GPU VRAM availability. 8B models typically respond in < 5 seconds on modern GPUs.
    *   **Ingestion:** The initial OCR process for large PDFs is resource-intensive but is mitigated by the caching strategy.
