FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
