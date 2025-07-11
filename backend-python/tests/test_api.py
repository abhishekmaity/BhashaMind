"""API tests for summarization and classification endpoints."""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_summarization():
    """Test the summarization endpoint with valid input."""
    text_to_summarize = (
        "প্যারিস জলবায়ু চুক্তি ২০১৫ সালে স্বাক্ষরিত হয়। "
        "এই চুক্তির মাধ্যমে বিশ্বের প্রায় সব দেশ গ্লোবাল ওয়ার্মিং কমাতে "
        "সম্মত হয়েছে। চুক্তির লক্ষ্য হলো গড় তাপমাত্রা বৃদ্ধি ২ ডিগ্রি "
        "সেলসিয়াসের নিচে রাখা এবং চেষ্টা করা যাতে ১.৫ ডিগ্রির মধ্যে "
        "সীমাবদ্ধ থাকে।"
    )
    # Line 13 was reported, applying noqa to the end of the multi-line string assignment
    response = client.post("/api/summarize", json={"text": text_to_summarize})
    assert response.status_code == 200
    assert "summary" in response.json()


def test_classification():
    """Test the classification endpoint with valid input."""
    text_to_classify = (
        "বিশ্ব অর্থনীতি ধীর গতিতে চলছে এবং মুদ্রাস্ফীতি, সুদের হার ও "
        "ভূরাজনৈতিক উত্তেজনা বিশ্ববাজারে প্রভাব ফেলছে।"
    )
    response = client.post("/api/classify", json={"text": text_to_classify})
    assert response.status_code == 200
    # Assuming the service returns a label, actual key might vary
    assert "label" in response.json() # Or more specific key if known


def test_summarization_empty():
    """Test the summarization endpoint with empty text."""
    response = client.post("/api/summarize", json={"text": ""})
    assert response.status_code == 400


def test_classification_empty():
    """Test the classification endpoint with empty text."""
    response = client.post("/api/classify", json={"text": ""})
    assert response.status_code == 400


def test_summarization_missing():
    """Test summarization with missing 'text' field."""
    response = client.post("/api/summarize", json={})
    assert response.status_code == 422  # Unprocessable Entity


def test_classification_missing():
    """Test classification with missing 'text' field."""
    response = client.post("/api/classify", json={})
    assert response.status_code == 422  # Unprocessable Entity


def test_summarize_non_string_input():
    """Test summarization with non-string input."""
    response = client.post("/api/summarize", json={"text": 12345})
    assert response.status_code == 422  # Unprocessable Entity

def test_summarization_error_short_text():
    response = client.post("/api/summarize", json={"text": "হেলো"})
    assert response.status_code == 400

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

