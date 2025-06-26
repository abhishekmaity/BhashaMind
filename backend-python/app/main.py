from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from .summarizer import summarize_text
from .classifier import classify_text

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/api/summarize")
def summarize(req: TextRequest):
    if not req.text or len(req.text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Input text too short for summarization.")
    try:
        summary = summarize_text(req.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization failed: {str(e)}")

@app.post("/api/classify")
def classify(req: TextRequest):
    if not req.text or len(req.text.strip()) < 5:
        raise HTTPException(status_code=400, detail="Input text too short for classification.")
    try:
        label = classify_text(req.text)
        return {"label": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Classification failed: {str(e)}")

@app.get("/health")
def health_check():
    return {"status": "ok"}
