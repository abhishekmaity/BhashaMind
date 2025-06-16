"""Module for text classification using a Hugging Face model."""

from transformers import pipeline  # Third-party import first
from .models import classifier_model  # Local import


# Initialize the classification pipeline
classifier = pipeline(
    "text-classification",
    model=classifier_model.MODEL_NAME,  # Removed trailing whitespace here
    tokenizer=classifier_model.tokenizer
)


def classify_text(text: str) -> dict:  # Changed return type hint to dict
    """
    Classifies the input text.

    Args:
        text: The text to classify.

    Returns:
        A dictionary containing the classification result (e.g., label and score).
    """
    result = classifier(text)
    return result[0]
