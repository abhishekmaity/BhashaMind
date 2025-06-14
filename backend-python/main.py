from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from transformers import pipeline
import logging

app = FastAPI()

# Logging setup
logging.basicConfig(level=logging.INFO)

# Define request model
class TextRequest(BaseModel):
    text: str

# Load models (use try/except in production for lazy-loading)
summarizer = pipeline("summarization", model="csebuetnlp/banglat5-small", tokenizer="csebuetnlp/banglat5-small")
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

@app.post("/api/summarize")
async def summarize(req: TextRequest):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    try:
        result = summarizer(text, max_length=60, min_length=10, do_sample=False)
        return {"summary": result[0]['summary_text']}
    except Exception as e:
        logging.error(f"Summarization failed: {e}")
        raise HTTPException(status_code=500, detail="Summarization model error.")

@app.post("/api/classify")
async def classify(req: TextRequest):
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    candidate_labels = ["economy", "politics", "health", "education", "sports", "technology"]
    try:
        result = classifier(text, candidate_labels)
        return {"label": result["labels"][0]}
    except Exception as e:
        logging.error(f"Classification failed: {e}")
        raise HTTPException(status_code=500, detail="Classification model error.")
