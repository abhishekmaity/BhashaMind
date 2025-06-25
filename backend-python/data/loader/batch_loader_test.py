import unittest
from batch_loader import load_tsv_file, validate_dataset
import pandas as pd

class TestBatchLoader(unittest.TestCase):

    def test_load_valid_file(self):
        df = load_tsv_file("data/sample_anandabazar.tsv")
        self.assertIsNotNone(df)
        self.assertGreater(len(df), 0)
        self.assertIn("headline", df.columns)

    def test_missing_column(self):
        df = pd.DataFrame({"headline": ["test"], "body_text": ["test"]})
        df.to_csv("data/invalid.tsv", sep="\t", index=False)
        result = load_tsv_file("data/invalid.tsv")
        self.assertIsNone(result)

    def test_bengali_validation(self):
        df = pd.DataFrame({
            "headline": ["শিক্ষা মন্ত্রী জানিয়েছেন..."],
            "body_text": ["আজ থেকে স্কুল খোলা হবে।"],
            "summary": ["স্কুল খোলার ঘোষণা।"],
            "category": ["শিক্ষা"]
        })
        errors = validate_dataset(df)
        self.assertEqual(len(errors), 0)

def validate_bengali_text(text):
    return isinstance(text, str) and any('\u0980' <= c <= '\u09FF' for c in text)

def validate_dataset(df):
    errors = []
    for idx, row in df.iterrows():
        for col in ['headline', 'body_text', 'category']:
            if not validate_bengali_text(row[col]):
                errors.append((idx, col))
    return errors


if __name__ == "__main__":
    unittest.main()
