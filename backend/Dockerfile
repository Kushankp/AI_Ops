# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy your source code
COPY . .

# Expose port (Cloud Run will override it with $PORT)
EXPOSE 8080

# Set environment variable fallback
ENV PORT 8080

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]
