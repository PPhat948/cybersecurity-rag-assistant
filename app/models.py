from typing import List
from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    """
    Request model for the chat endpoint.
    """
    question: str = Field(
        ..., 
        description="The question to ask the RAG system.",
        example="What are the common vulnerabilities in web applications?"
    )

class AnswerWithCitation(BaseModel):
    """
    Response model containing the generated answer and cited sources.
    """
    answer: str = Field(
        ..., 
        description="The generated answer from the LLM based on the context."
    )
    sources: List[str] = Field(
        ..., 
        description="List of source filenames cited in the answer."
    )
