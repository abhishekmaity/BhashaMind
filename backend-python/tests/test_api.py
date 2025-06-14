from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_summarization():
    response = client.post("/api/summarize", json={
        "text": "প্যারিস জলবায়ু চুক্তি ২০১৫ সালে স্বাক্ষরিত হয়। এই চুক্তির মাধ্যমে বিশ্বের প্রায় সব দেশ গ্লোবাল ওয়ার্মিং কমাতে সম্মত হয়েছে। চুক্তির লক্ষ্য হলো গড় তাপমাত্রা বৃদ্ধি ২ ডিগ্রি সেলসিয়াসের নিচে রাখা এবং চেষ্টা করা যাতে ১.৫ ডিগ্রির মধ্যে সীমাবদ্ধ থাকে।"
    })
    assert response.status_code == 200
    assert "summary" in response.json()

def test_classification():
    response = client.post("/api/classify", json={
        "text": "বিশ্ব অর্থনীতি ধীর গতিতে চলছে এবং মুদ্রাস্ফীতি, সুদের হার ও ভূরাজনৈতিক উত্তেজনা বিশ্ববাজারে প্রভাব ফেলছে।"
    })
    assert response.status_code == 200
    assert "label" in response.json()

def test_summarization_empty():
    response = client.post("/api/summarize", json={"text": ""})
    assert response.status_code == 400

def test_classification_empty():
    response = client.post("/api/classify", json={"text": ""})
    assert response.status_code == 400

def test_summarization_missing():
    response = client.post("/api/summarize", json={})
    assert response.status_code == 422

def test_classification_missing():
    response = client.post("/api/classify", json={})
    assert response.status_code == 422

def test_summarize_non_string_input():
    response = client.post("/api/summarize", json={"text": 12345})
    assert response.status_code == 422
