FROM python:3.11-slim

RUN pip install --no-cache-dir fastapi uvicorn

WORKDIR /app

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
