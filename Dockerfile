# ---------- Base Python image ----------
FROM python:3.11-slim

# ---------- Set working directory ----------
WORKDIR /app

# ---------- Install system dependencies (optional for psycopg2) ----------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ---------- Copy only requirements first (Docker caching) ----------
COPY requirements.txt .

# ---------- Install dependencies ----------
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy full project ----------
COPY . .

# ---------- Expose FastAPI port ----------
EXPOSE 8000

# ---------- Run the app ----------
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
