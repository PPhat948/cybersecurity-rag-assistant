# Cybersecurity RAG Assistant

> **A strictly grounded, offline-capable AI assistant for cybersecurity queries, powered by Llama 3.1 and Typhoon OCR.**

## Overview
This project serves as a **Retrieval-Augmented Generation (RAG)** assessment. It is designed to answer questions based **strictly** on provided local cybersecurity datasets.

Unlike general-purpose chatbots, this assistant:
1.  **Refuses** to answer if the information is not in its knowledge base.
2.  **Cites** the specific source file for every claim it makes.
3.  **Runs entirely offline** using local embeddings and LLMs, complying with strict data privacy requirements.
4.  **Digitizes Thai PDFs** using state-of-the-art OCR (Typhoon 1.5) to ensure high-quality retrieval.

## Key Features
*   **Privacy-First & Offline:** Runs locally using Docker and Ollama. No data leaves your infrastructure.

*   **Precise Citations:** Returns the exact filename (e.g., `OWASP_Top_10.md`) used to generate the answer.
*   **GPU Accelerated:** Configured to leverage NVIDIA GPUs for both LLM inference and OCR processing.
*   **Persistent Caching:** Models (Ollama, HuggingFace) are cached on the host machine to prevent unnecessary re-downloads.

## Project Structure

```text
cybersecurity-rag/
├── app/
│   ├── api.py          # FastAPI application entry point
│   ├── ingestion.py    # Document processing (Typhoon OCR) and vector indexing
│   ├── models.py       # Pydantic data models
│   └── rag_engine.py   # Core RAG logic and LLM interaction
├── dataset/            # Directory for source documents (.md, .pdf)
├── hf_cache/           # Local cache for HuggingFace models (Embeddings)
├── ollama_cache/       # Local cache for Ollama models (Llama 3.1)
├── docker-compose.yml  # Docker services configuration
├── Dockerfile          # Container image definition
├── entrypoint.sh       # Startup script for Ollama and API
└── requirements.txt    # Python dependencies
```

## Tech Stack
*   **Language:** Python 3.10+
*   **LLM:** Llama-3.1-8B-Instruct (4-bit quantized)
*   **OCR:** Typhoon OCR 1.5 (2B Vision-Language Model)
*   **Orchestrator:** LangChain
*   **Vector DB:** FAISS (CPU)
*   **API:** FastAPI
*   **Build Tool:** uv

## Quick Start

### Prerequisites
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
*   [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) installed (Required for GPU acceleration).

### 1. Start the System
The system is containerized for easy deployment. It will automatically download necessary models (Llama 3.1, Typhoon OCR, BGE-M3) on the first run.

```bash
docker-compose up
```
*(Note: Use `docker-compose up --build` if you have modified requirements or Dockerfile)*

### 2. Ingest Data
Once the container is running and the API is live, you need to build the vector index.
*On the first run, this will perform OCR on all PDFs (which may take time). Future runs will be instant due to caching.*

```bash
docker-compose exec rag-app python app/ingestion.py
```

## Usage

### Method 1: API (Recommended)
*   **Swagger UI:** Open [http://localhost:8000/docs](http://localhost:8000/docs)
*   **Example Request:**

```json
POST /chat
{
  "question": "What is Broken Access Control?"
}
```

### Method 2: CLI
For direct interaction within the container:

```bash
docker exec -it cybersecurity_rag python cli.py
```

## Running the Evaluation
To verify the system's performance against predefined test cases (including OWASP, MITRE, and Thai documents), use the provided Jupyter notebook.

1.  **Ensure Requirements are Met:**
    The notebook requires `requests` to communicate with the API.
    ```bash
    pip install requests
    ```
    *(Alternatively, the first cell of the notebook contains a magic command to install this for you.)*

2.  **Open the Notebook:**
    ```bash
    jupyter notebook notebooks/evaluation_example.ipynb
    ```

3.  **Run All Cells:**
    Execute the cells to see real-time query results, including answers, citations, and response times.



##  Deliverables Map

| Requirement | Location |
| :--- | :--- |
| **1. Working Prototype** | `app/` (Run via `docker-compose up`) |
| **2. Architecture Explanation** | [ARCHITECTURE.md](ARCHITECTURE.md) |
| **3. System Diagram** | [ARCHITECTURE.md](ARCHITECTURE.md#system-diagram) |
| **4. Evaluation Examples** | [notebooks/evaluation_example.ipynb](notebooks/evaluation_example.ipynb) |
| **5. Source Code** | `app/` directory |

---
*Built for the Datafarm Cybersecurity RAG Assessment.*
