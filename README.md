Project Overview: AI Chat Agent for Uploaded PDFs
Tech Stack:

Frontend: React

Backend: FastAPI (Python)

LLM: Groq API (llama3-70b-8192)

Vector DB: Pinecone

Embeddings: Locally stored all-MiniLM-L6-v2

Deployment: Cloud Run

Infrastructure Tools: Docker, .env, CORS

🧠 Core Features Implemented
PDF Upload with vectorization using HuggingFace embeddings

Context-based retrieval using LangChain & Pinecone

LLM-powered answer generation based on query + retrieved context

Deployed containerized FastAPI backend to Google Cloud Run

React frontend that sends questions and displays answers

Verified local embedding model to work offline for Cloud Run
