# Shoutout to those guys here : https://docs.streamlit.io/deploy/tutorials/docker

# Get python version
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# RUN apt update && apt install -y curl
# 
# COPY requirements.txt .
# 
# RUN python3 -m venv .venv && source ./.venv/bin/activate && pip install streamlit