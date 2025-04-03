FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=80

COPY src/ .

CMD ["python", "app.py"]