from transformers import pipeline

# Load zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

# Example candidate labels (can be customized for Bengali topics)
candidate_labels = ["রাজনীতি", "খেলাধুলা", "অর্থনীতি", "স্বাস্থ্য", "প্রযুক্তি"]

def classify_text(text: str) -> str:
    result = classifier(text, candidate_labels=candidate_labels)
    return result['labels'][0]
