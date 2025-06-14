from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Sample inference pipelines (simulate pre-loaded models)
summarizer = pipeline("summarization", model="csebuetnlp/banglat5-small", tokenizer="csebuetnlp/banglat5-small")
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

class TextRequest(BaseModel):
    text: str

@app.post("/api/summarize")
async def summarize(request: TextRequest):
    summary = summarizer(request.text, max_length=60, min_length=10, do_sample=False)[0]["summary_text"]
    return {"summary": summary}

@app.post("/api/classify")
async def classify(request: TextRequest):
    candidate_labels = ["economy", "education", "politics", "environment", "health"]
    result = classifier(request.text, candidate_labels)
    return {"label": result["labels"][0]}
