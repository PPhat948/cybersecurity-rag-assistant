#!/bin/bash
set -e

# 1. Start Ollama in the background
echo "Starting Ollama service..."
ollama serve &

# 2. Wait for Ollama to be ready
echo "Waiting for Ollama to be ready..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
    sleep 1
done
echo "Ollama is ready."

# 3. Check for the model and pull if missing
MODEL_NAME="llama3.1:8b"
if ! ollama list | grep -q "$MODEL_NAME"; then
    echo "Model '$MODEL_NAME' not found. Pulling..."
    ollama pull "$MODEL_NAME"
    echo "Model pulled successfully."
else
    echo "Model '$MODEL_NAME' already exists."
fi

# 3.5 Run Ingestion (added to automate RAG index creation)
echo "Running ingestion..."
python app/ingestion.py

# 4. Start the FastAPI application
echo "Starting FastAPI app..."
# We use 'app.api:app' assuming the structure app/api.py
exec uvicorn app.api:app --host 0.0.0.0 --port 8000
