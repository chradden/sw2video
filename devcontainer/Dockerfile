# Basis: Python 3.9 mit Debian
FROM python:3.9-slim

# System-Abhängigkeiten
RUN apt-get update && apt-get install -y \
    libgl1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Python-Abhängigkeiten
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# User-Konfiguration
ENV PYTHONUNBUFFERED=1
