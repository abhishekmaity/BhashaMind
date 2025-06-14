from .models import summarizer_model
from transformers import pipeline

summarizer = pipeline("summarization", model=summarizer_model.model, tokenizer=summarizer_model.tokenizer)

def summarize_text(text: str) -> str:
    summary = summarizer(text, max_length=128, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

