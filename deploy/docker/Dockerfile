# Placeholder build file for the Neon-Ai stack.
# Extend this with the packages and runtime needed for Open WebUI/Ollama orchestration.

FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Base application code and config
COPY src/ ./src
COPY models/model_list.yaml ./models/model_list.yaml
COPY src/config ./src/config

# TODO: install runtime dependencies once they are defined
# RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "src.main"]
