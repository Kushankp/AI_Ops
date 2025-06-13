from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load env variables

app = FastAPI()

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
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": request.message}
        ],
        "temperature": 0.7
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    
    print("🔍 Raw Response:")
    print(response.status_code)
    print(response.text)  # Add this to inspect the response

    try:
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e), "raw_response": response.text}
