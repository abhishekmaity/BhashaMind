import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust path based on your app structure

client = TestClient(app)

# -------- Test Summarization --------
def test_summarize_valid_input():
    payload = {
        "text": "বাংলাদেশের রাজধানী ঢাকা একটি জনবহুল শহর। এটি দেশের প্রশাসনিক ও অর্থনৈতিক কেন্দ্র।"
    }
    response = client.post("/api/summarize", json=payload)
    assert response.status_code == 200
    assert "summary" in response.json()

def test_summarize_empty_input():
    response = client.post("/api/summarize", json={"text": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Text cannot be empty."

def test_summarize_missing_field():
    response = client.post("/api/summarize", json={})
    assert response.status_code == 422  # Pydantic validation

# -------- Test Classification --------
def test_classify_valid_input():
    payload = {
        "text": "আন্তর্জাতিক মুদ্রা তহবিল জানিয়েছে বৈশ্বিক অর্থনীতি দুর্বল হচ্ছে।"
    }
    response = client.post("/api/classify", json=payload)
    assert response.status_code == 200
    assert "label" in response.json()

def test_classify_empty_input():
    response = client.post("/api/classify", json={"text": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Text cannot be empty."

def test_classify_missing_field():
    response = client.post("/api/classify", json={})
    assert response.status_code == 422
