FROM python:3.11-slim

RUN apt update && apt install -y curl

COPY requirements.txt .

RUN python3 -m venv .venv && source ./.venv/bin/activate && pip install streamlit