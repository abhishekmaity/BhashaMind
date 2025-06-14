from .models import classifier_model
from transformers import pipeline

classifier = pipeline("text-classification", model=classifier_model.model, tokenizer=classifier_model.tokenizer)

def classify_text(text: str) -> str:
    result = classifier(text)
    return result[0]
