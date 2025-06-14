from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Seq2SeqTrainer, Seq2SeqTrainingArguments
from utils.preprocessing import load_bengali_dataset

model_name = "google/mt5-small"
dataset = load_bengali_dataset("summarization")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def preprocess(examples):
    inputs = tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)
    targets = tokenizer(examples["summary"], truncation=True, padding="max_length", max_length=128)
    inputs["labels"] = targets["input_ids"]
    return inputs

tokenized = dataset["train"].map(preprocess, batched=True)

args = Seq2SeqTrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=1,
    logging_dir="./logs",
    save_total_limit=1
)

trainer = Seq2SeqTrainer(
    model=model,
    args=args,
    train_dataset=tokenized,
)

trainer.train()
