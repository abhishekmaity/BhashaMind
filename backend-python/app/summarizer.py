"""Module for text summarization using a Hugging Face model."""

from transformers import pipeline  # Third-party import first
from .models import summarizer_model  # Local import


# Initialize the summarization pipeline
summarizer = pipeline(  # noqa: E501
    "summarization",
    model=summarizer_model.MODEL_NAME,
    tokenizer=summarizer_model.tokenizer
)


def summarize_text(text: str) -> str:
    """
    Summarizes the input text.

    Args:
        text: The text to summarize.

    Returns:
        The summarized text.
    """
    summary = summarizer(text, max_length=128, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
