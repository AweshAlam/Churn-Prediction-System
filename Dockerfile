# ✅ Stable & compatible with sklearn + xgboost
FROM python:3.9-slim

# Prevent .pyc files & enable real-time logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# ✅ System dependencies for numpy / scipy / xgboost
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better Docker caching)
COPY requirements.txt .

# Upgrade pip & install Python dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Render provides PORT automatically
CMD ["python", "app.py"]
