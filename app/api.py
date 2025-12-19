from fastapi import FastAPI, HTTPException
from app.models import QueryRequest, AnswerWithCitation
from app.rag_engine import generate_answer
import os

app = FastAPI(title="Cybersecurity RAG API")

@app.get("/")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok", "service": "Cybersecurity RAG API"}

@app.post("/chat", response_model=AnswerWithCitation)
def chat_endpoint(request: QueryRequest):
    """
    Chat endpoint to answer questions using RAG.
    """
    try:
        # Check if FAISS index exists before attempting to answer
        if not os.path.exists("./faiss_index"):
             raise HTTPException(
                status_code=500, 
                detail="FAISS index not found. Please run ingestion first."
            )

        response = generate_answer(request.question)
        return response
    except Exception as e:
        # Log the full error
        print(f"API Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
