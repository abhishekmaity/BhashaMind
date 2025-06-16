"""API router for text summarization."""

from fastapi import APIRouter
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

router = APIRouter()


# Load model and tokenizer (BanglaT5)
# These should ideally be loaded once globally, not per module import,
# but following current structure for now.
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_small", use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_small")


class SummarizationRequest(BaseModel):
    """Request model for summarization."""
    text: str


class SummarizationResponse(BaseModel):
    """Response model for summarization."""
    summary: str


@router.post("/summarize", response_model=SummarizationResponse)
async def summarize_text_endpoint(request: SummarizationRequest):
    """
    Summarizes the input text using a preloaded model.
    """
    inputs = tokenizer.encode(
        "summarize: " + request.text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )
    summary_ids = model.generate(
        inputs,
        max_length=100,
        min_length=20,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return SummarizationResponse(summary=summary)
