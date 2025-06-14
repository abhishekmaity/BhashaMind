# backend-python/app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer import generate_summary
from classifier import classify_text

app = FastAPI(title="BhashaMind NLP API", version="0.1")

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(req: TextRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text input is empty")
    return {"summary": generate_summary(req.text)}

@app.post("/classify")
def classify(req: TextRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text input is empty")
    return {"category": classify_text(req.text)}
