from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload
from pydantic import BaseModel
import requests
import os
from agent.rag_chain import get_context_for_query

app = FastAPI()
app.include_router(upload.router)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-ops.pages.dev/"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Your Groq AI Agent is Running 🚀"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # 🔍 Step 1: Get relevant context using RAG
        context = get_context_for_query(request.message)

        # 🔁 Step 2: Build prompt
        if context.strip():
            prompt = f"""
You are an intelligent assistant. If the provided context is useful, use it to answer the question. Otherwise, answer from your own knowledge.

--- Context ---
{context}
----------------

User Question: {request.message}
"""
        else:
            prompt = f"""
You are an intelligent assistant. Answer the following question based on your knowledge:

User Question: {request.message}
"""

        # 🔐 Step 3: Call Groq API
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "Be helpful, accurate, and detailed."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )

        result = response.json()
        print("🔁 Groq Response:", result)

        # 🧠 Step 4: Return LLM answer
        if "choices" in result:
            reply = result["choices"][0]["message"]["content"]
            return {"reply": reply}
        elif "error" in result:
            return {"error": result["error"].get("message", "Unknown error from Groq")}
        else:
            return {"error": "Unexpected response from Groq API"}

    except Exception as e:
        print("❌ Error during chat:", e)
        return {"error": str(e)}
