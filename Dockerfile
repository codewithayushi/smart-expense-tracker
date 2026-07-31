# Python ka official light image lo
FROM python:3.10-slim

# Working directory set karo
WORKDIR /app

# Requirements file copy karo aur dependencies install karo
COPY requirements.txt .
RUn pip install --no-cache-dir -r requirements.txt

# Baaki sara code copy karo
COPY . .

# Server run karne ka command
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]