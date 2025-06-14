# backend-python/app/classifier.py

from transformers import pipeline

# Bengali-compatible zero-shot classification (placeholder)
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

LABELS = ["রাজনীতি", "খেলাধুলা", "স্বাস্থ্য", "শিক্ষা", "অর্থনীতি", "বিনোদন", "প্রযুক্তি"]

def classify_text(text: str) -> str:
    result = classifier(text, candidate_labels=LABELS)
    return result["labels"][0]
