from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/mt5-small"  # Or your fine-tuned checkpoint path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
