# backend-python/app/routers/summarize.py

from fastapi import APIRouter
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

router = APIRouter()

# Load model and tokenizer (BanglaT5)
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5-small")

class SummarizationRequest(BaseModel):
    text: str

class SummarizationResponse(BaseModel):
    summary: str

@router.post("/summarize", response_model=SummarizationResponse)
async def summarize_text(request: SummarizationRequest):
    inputs = tokenizer.encode("summarize: " + request.text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=100, min_length=20, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return SummarizationResponse(summary=summary)
