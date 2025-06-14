# backend-python/app/summarizer.py

from transformers import pipeline

# Bengali-compatible summarization pipeline
summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")

def generate_summary(text: str) -> str:
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']
