"""Router for text classification."""

from fastapi import APIRouter
from pydantic import BaseModel
from app.classifier import classify_text

router = APIRouter()


class ClassificationRequest(BaseModel):
    """Request model for classification."""
    text: str


class ClassificationResponse(BaseModel):
    """Response model for classification."""
    label: str
    score: float


@router.post("/classify", response_model=ClassificationResponse)
async def classify_text_endpoint(request: ClassificationRequest):
    """
    Endpoint to classify text.
    Receives text and returns its classification label and score.
    """
    # The classify_text function is expected to return a dict like {'label': 'LABEL_X', 'score': 0.99}
    # based on the previous understanding that it returns result[0] from a pipeline.
    classification_result = classify_text(request.text)
    return classification_result
