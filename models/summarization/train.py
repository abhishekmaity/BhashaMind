from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Seq2SeqTrainer, Seq2SeqTrainingArguments
from utils.preprocessing import load_bengali_dataset

model_name = "google/mt5-small"
dataset = load_bengali_dataset("summarization") # This loads the entire dataset dictionary

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def preprocess(examples):
    inputs = tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512, return_tensors="pt")
    # For summarization, the 'summary' field is typically the target
    targets = tokenizer(examples["summary"], truncation=True, padding="max_length", max_length=128, return_tensors="pt")
    inputs["labels"] = targets["input_ids"]
    return inputs

# Tokenize the training and evaluation datasets
tokenized_train = dataset["train"].map(preprocess, batched=True)

eval_split_name = None
if "validation" in dataset:
    eval_split_name = "validation"
elif "test" in dataset:
    eval_split_name = "test"

tokenized_eval = None
if eval_split_name:
    tokenized_eval = dataset[eval_split_name].map(preprocess, batched=True)
else:
    # Fallback or error if no suitable validation/test split is available
    # For this exercise, we'll assume one exists or Trainer will handle a None eval_dataset.
    # evaluation_strategy="epoch" would require an eval_dataset.
    print(f"Warning: Neither 'validation' nor 'test' split found in dataset. Evaluation will be skipped or may fail.")


args = Seq2SeqTrainingArguments(
    output_dir="./results-summarization", # Changed output_dir to avoid conflict with classification
    per_device_train_batch_size=2,    # Default is 2, can be adjusted based on GPU memory
    per_device_eval_batch_size=2,     # Added for evaluation
    num_train_epochs=1,               # Keeping it to 1 epoch for quick runs
    logging_dir="./logs-summarization",   # Changed logging_dir
    save_total_limit=1,
    evaluation_strategy="epoch",      # Evaluate at the end of each epoch
    logging_strategy="epoch",         # Log at the end of each epoch
    load_best_model_at_end=True,      # Load the best model found during training
    metric_for_best_model="loss",     # Use loss to determine the best model
    predict_with_generate=True        # Important for Seq2Seq tasks for text generation based metrics
)

trainer = Seq2SeqTrainer(
    model=model,
    args=args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_eval        # Add evaluation dataset
)

trainer.train()
