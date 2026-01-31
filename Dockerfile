# Use Python 3.9 (fixed, legacy-safe)
FROM python:3.9-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (needed for scipy & xgboost)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Upgrade pip & install dependencies
RUN pip install --upgrade pip setuptools \
    && pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render uses $PORT)
EXPOSE 8000

# Start the Flask app
CMD ["python", "app.py"]
