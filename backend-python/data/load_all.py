# backend-python/data/load_all.py

import pandas as pd
from pathlib import Path

RAW_DIR = Path(__file__).parent / "raw"
PROCESSED_DIR = Path(__file__).parent / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def clean_text(text):
    return str(text).replace("\n", " ").strip()

def process_tsv(file_path):
    df = pd.read_csv(file_path, sep="\t")
    if not {"headline", "body", "category"}.issubset(df.columns):
        print(f"⚠️ Skipping {file_path.name} (missing required columns)")
        return
    
    df["headline"] = df["headline"].apply(clean_text)
    df["body"] = df["body"].apply(clean_text)
    df["text"] = df["headline"] + " " + df["body"]
    
    output_file = PROCESSED_DIR / (file_path.stem + ".jsonl")
    df[["text", "category"]].to_json(output_file, orient="records", lines=True, force_ascii=False)
    print(f"✅ Processed: {file_path.name} → {output_file.name}")

def main():
    print("🔍 Batch loading TSV files...")
    for file in RAW_DIR.glob("*.tsv"):
        process_tsv(file)
    print("✅ All files processed.")

if __name__ == "__main__":
    main()
