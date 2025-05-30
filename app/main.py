# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.qa_engine import generate_answer

app = FastAPI()

class Query(BaseModel):
    question: str
    image: str | None = None

@app.post("/api/")
async def answer(query: Query):
    return generate_answer(query.question, query.image)
