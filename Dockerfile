FROM python:3.13.2-alpine3.21

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    apk add --update --no-cache \
        gcc \
        libc-dev \
        mariadb-dev && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000