FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd appuser && chown -R appuser /usr/src/app
USER appuser

# Gunicorn will serve the app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

