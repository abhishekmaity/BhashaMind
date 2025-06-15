"""Main FastAPI application for BhashaMind NLP services."""

from fastapi import FastAPI
from app.routers import summarize

app = FastAPI(
    title="BhashaMind NLP API",
    description="Summarization and classification for Bengali text",
    version="1.0.0",
)

app.include_router(summarize.router, prefix="/api")
