from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")

def summarize_text(text: str) -> str:
    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']
