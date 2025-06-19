# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional but often needed)
RUN apt-get update && apt-get install -y git && apt-get clean

# Copy requirements first for better Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Copy the local embedding model into the container (you renamed this to local_model)
COPY ./local_model /app/local_model

# Expose port (Cloud Run sets $PORT, but this is fallback)
ENV PORT 8080

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]
