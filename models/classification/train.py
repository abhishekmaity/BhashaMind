from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from utils.preprocessing import load_bengali_dataset

model_name = "ai4bharat/indic-bert"
dataset = load_bengali_dataset("classification")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

tokenized = dataset["train"].map(preprocess, batched=True)

args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=4,
    num_train_epochs=1,
    logging_dir="./logs",
    save_total_limit=1
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized,
)

trainer.train()
