FROM python:3.10-slim

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      gcc \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 8000

CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn bestStone.wsgi:application --bind 0.0.0.0:8000 --workers 3"]
