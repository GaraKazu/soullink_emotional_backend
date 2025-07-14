# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from noel_ai import get_noel_response

app = FastAPI()

# Allow CORS for frontend or other origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this to your frontend's URL in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    user_text = message.text.strip()
    response = get_noel_response(user_text)
    return {"response": response}

