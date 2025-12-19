# System Architecture

## Overview
The Cybersecurity RAG Assistant is designed as a standalone, containerized application that leverages offline Large Language Models (LLMs) and Vision-Language Models (VLMs) to answer domain-specific queries with high accuracy and strict grounding.

## System Diagram

<!-- Paste your system diagram image here -->

### 1. Data Ingestion & OCR
*   **Input:** User-provided documents in `./dataset` (Markdown and PDF formats).
*   **OCR Processing:**
    *   **Vision Model:** The system uses `scb10x/typhoon-ocr1.5-2b` (a 2-billion parameter VLM) to process PDF files.
    *   **Process:** PDF pages are rendered into images using `PyMuPDF` and then passed to the Typhoon model to generate markdown-formatted text.
*   **Text Splitting:** Processed text is split into chunks of 1000 characters with a 200-character overlap using `RecursiveCharacterTextSplitter`.
*   **Embeddings:** Chunks are converted into vector embeddings using `BAAI/bge-m3` (running locally via HuggingFace).
*   **Vector Store:** Vectors are indexed and stored locally using `FAISS`.

### 2. Retrieval Engine
*   **Query Analysis:** User questions are converted into embeddings using the same `BAAI/bge-m3` model.
*   **Similarity Search:** FAISS retrieves the Top-K (default: 4) most relevant text chunks based on cosine similarity.
*   **Score Threshold:** (Implicit) The retriever ranks documents by relevance to ensure quality context injection.

### 3. Generation Engine (RAG)
*   **LLM:** `Llama-3.1-8B-Instruct` (4-bit quantized) running on `Ollama`.
*   **Prompt Engineering:**
    *   **System Prompt:** Enforces a persona of a cybersecurity expert.
    *   **Constraints:** Strictly instructs the model to answer *only* from the provided context and to output "I don't know" if the answer is missing.
    *   **Citation Requirement:** Mandates that every answer must refer to specific source files found in the metadata.
*   **Output:** The model generates a structured JSON response containing the answer string and a list of source filenames.

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
