from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "ai4bharat/indic-bert"  # Or your fine-tuned checkpoint path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
