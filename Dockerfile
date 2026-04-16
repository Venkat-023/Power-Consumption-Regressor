FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=7860
ENV API_BASE_URL=http://127.0.0.1:8000

WORKDIR /app

COPY Backend/requirements.txt /tmp/backend-requirements.txt
COPY Frontend/requirements.txt /tmp/frontend-requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/backend-requirements.txt -r /tmp/frontend-requirements.txt

COPY Backend /app/Backend
COPY Frontend /app/Frontend

EXPOSE 7860

CMD ["sh", "-c", "uvicorn Backend.app:app --host 0.0.0.0 --port 8000 & exec streamlit run Frontend/app.py --server.address=0.0.0.0 --server.port=${PORT:-7860}"]
