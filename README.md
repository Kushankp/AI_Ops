# 🧠 AI Chat Agent for Uploaded PDFs

This project enables users to upload PDFs and query them via a chat interface. It combines local embedding generation, vector search, and large language models (LLMs) to deliver intelligent answers grounded in the uploaded documents.

---

## 🚀 Tech Stack

- **Frontend**: React  
- **Backend**: FastAPI (Python)  
- **LLM**: Groq API(`llama3-70b-8192`)  
- **Vector DB**: Pinecone
- **Embeddings**: Locally stored [`all-MiniLM-L6-v2`]
- **Deployment**: Google Cloud Run  
- **Infrastructure Tools**: Docker, `.env`, CORS

---

## ✅ Core Features

- 📄 **PDF Upload & Vectorization**  
  Extracts and embeds text locally using HuggingFace Sentence Transformers.

- 🔍 **Contextual Retrieval with Pinecone**  
  Uses LangChain + Pinecone to retrieve relevant chunks from the uploaded document.

- 🤖 **LLM-based Answer Generation**  
  Sends the query and retrieved context to Groq’s LLaMA3 model for accurate, context-aware answers.

- ☁️ **Cloud Deployment**  
  FastAPI backend is containerized and deployed via Google Cloud Run for scalability.

- 🧑‍💻 **Interactive Frontend**  
  Simple React interface that accepts user queries and displays model responses.

- 🔌 **Offline Embeddings for Cloud Run**  
  The model is bundled in the Docker image to avoid outbound internet dependency in Cloud Run environments.
