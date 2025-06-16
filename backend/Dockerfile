# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire app source code
COPY . .

# Copy the locally downloaded embedding model into /app/models
# (Make sure this directory exists and has the model in it!)
COPY ./models /app/models

# Expose port (Cloud Run will override this with $PORT)
EXPOSE 8080

# Set fallback environment variable for PORT
ENV PORT 8080

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8080"]
