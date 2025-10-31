from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from src.ia.gemini import Gemini

import os

#--- Inicialização ---#
app = FastAPI()

load_dotenv()  # Carrega as variáveis do .env

#--- IA Configuração ---#
def load_system_prompt() -> str:
    try:
        with open("prompts/system_prompt.md", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None

system_prompt = load_system_prompt()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in environment variables.")

ia_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)

#--- Pydantic models ---#
class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    response: str

#--- endpoints ---#
@app.get("/")
async def root():
    return {"message": "Resume AI is running!"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response_text = ia_platform.chat(request.prompt)
    return ChatResponse(response=response_text)
