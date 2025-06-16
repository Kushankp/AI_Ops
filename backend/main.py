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
    allow_origins=["https://ai-ops.pages.dev"],  # Ensure it's a list
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
        context = get_context_for_query(request.message)

        prompt = f"""
You are an assistant helping the user based on the following context:

--- Context ---
{context}
----------------

Now answer the question: {request.message}
"""

        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama3-70b-8192",
            "messages": [
                {"role": "system", "content": "Only answer based on the context provided. Be precise."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        result = response.json()

        # Log full response for debugging
        print("🔁 Groq Response:", result)

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
