# backend-python/data/load_data.py

import pandas as pd
from pathlib import Path

RAW_DATA = Path(__file__).parent / "raw" / "anandabazar_sample.tsv"
PROCESSED_DIR = Path(__file__).parent / "processed"
PROCESSED_FILE = PROCESSED_DIR / "anandabazar_cleaned.jsonl"

def clean_text(text):
    return text.replace('\n', ' ').strip()

def load_and_clean():
    df = pd.read_csv(RAW_DATA, sep="\t")
    df = df.dropna(subset=["headline", "body"])
    df["headline"] = df["headline"].apply(clean_text)
    df["body"] = df["body"].apply(clean_text)
    df["text"] = df["headline"] + " " + df["body"]
    
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df[["text", "category"]].to_json(PROCESSED_FILE, orient="records", lines=True, force_ascii=False)
    
    print(f"✅ Saved cleaned dataset to: {PROCESSED_FILE}")

if __name__ == "__main__":
    load_and_clean()
