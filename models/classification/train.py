from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from utils.preprocessing import load_bengali_dataset

model_name = "ai4bharat/indic-bert"
dataset = load_bengali_dataset("classification") # This loads the entire dataset dictionary

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5) # Assuming 5 labels for this dataset

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

# Tokenize the training and test (validation) datasets
tokenized_train = dataset["train"].map(preprocess, batched=True)
# Assuming 'test' split exists and will be used for validation
if "test" in dataset:
    tokenized_eval = dataset["test"].map(preprocess, batched=True)
else:
    # Fallback or error if 'test' split is not available
    # For this exercise, we'll assume it exists or Trainer will handle a None eval_dataset gracefully if not set.
    # However, evaluation_strategy="epoch" would require an eval_dataset.
    # A more robust solution would be to split the train set if no test/validation set is available.
    print("Warning: 'test' split not found in dataset. Evaluation will be skipped or may fail.")
    tokenized_eval = None


args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,
    num_train_epochs=1,           # Keeping it to 1 epoch for quick runs; can be increased
    logging_dir="./logs",
    save_total_limit=1,
    evaluation_strategy="epoch",  # Evaluate at the end of each epoch
    logging_strategy="epoch",     # Log at the end of each epoch
    load_best_model_at_end=True,  # Load the best model found during training at the end
    metric_for_best_model="loss"  # Use loss to determine the best model (lower is better)
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_train,
    eval_dataset=tokenized_eval    # Add evaluation dataset
)

trainer.train()
