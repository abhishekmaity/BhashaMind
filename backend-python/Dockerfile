FROM python:3.10-slim
WORKDIR /app

ARG APP_USER=appuser
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY app ./app
COPY utils ./utils
# Assuming models and tests are not strictly needed for the runtime image
# If they were, they'd be added here:
# COPY models ./models
# COPY tests ./tests

USER $APP_USER
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
