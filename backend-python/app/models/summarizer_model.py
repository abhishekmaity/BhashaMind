"""Module defining the summarizer model and tokenizer."""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/mt5-small"  # Or your fine-tuned checkpoint path
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
