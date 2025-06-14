"""Module defining the classifier model and tokenizer."""

from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "ai4bharat/indic-bert"  # Or your fine-tuned checkpoint path
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
