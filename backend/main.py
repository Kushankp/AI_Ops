from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from agent.rag_chain import get_context_for_query  # make sure path is correct


load_dotenv()  # Load env variables

app = FastAPI()
app.include_router(upload.router)
# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend URL in prod
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
        # Step 1: Retrieve relevant document context
        context = get_context_for_query(request.message)

        # Step 2: Prepare prompt for Groq
        prompt = f"""
You are an assistant helping the user based on the following context:

--- Context ---
{context}
----------------

Now answer the question: {request.message}
"""

        # Step 3: Call Groq API
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
        reply = result["choices"][0]["message"]["content"]
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}
