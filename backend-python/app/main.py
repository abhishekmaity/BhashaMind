from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .summarizer import summarize_text
from .classifier import classify_text

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_endpoint(input_data: InputText):
    try:
        summary = summarize_text(input_data.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/classify")
async def classify_endpoint(input_data: InputText):
    try:
        label = classify_text(input_data.text)
        return {"label": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
