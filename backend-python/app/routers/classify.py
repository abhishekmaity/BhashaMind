"""Router for text classification."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.classifier import classify_text

from app.utils.prompt_templates import get_zero_shot_prompt

candidate_labels = ["অর্থনীতি", "রাজনীতি", "স্বাস্থ্য", "খেলাধুলা"]
hypotheses = [get_zero_shot_prompt(label, lang="bn") for label in candidate_labels]

router = APIRouter()


class ClassificationRequest(BaseModel):
    """Request model for classification."""
    text: str


class ClassificationResponse(BaseModel):
    """Response model for classification."""
    label: str
    score: float


@router.post(
    "/classify",
    response_model=ClassificationResponse
)
async def classify_text_endpoint(request: ClassificationRequest):
    """
    Endpoint to classify text.
    Receives text and returns its classification label and score.
    """
    if not request.text or request.text.isspace():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    # classify_text is expected to return a dict like {'label': 'LABEL_X', 'score': 0.99},
    # as it's assumed to return result[0] from a Hugging Face pipeline.
    classification_result = classify_text(request.text)
    return classification_result
