FROM python:3.11-slim

WORKDIR /app

COPY backend /app
COPY data /app/data

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]