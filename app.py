# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.ia.gemini import Gemini
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime

import os
import PyPDF2

#--- Inicialização ---#
app = FastAPI()

#--- Request Log Storage ---#
request_logs = []

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Registra: timestamp, método, rota e status
        log_entry = f"{datetime.now().strftime('%H:%M:%S')} - {request.method} {request.url.path} - {response.status_code}"
        request_logs.append(log_entry)
        
        return response

app.add_middleware(LoggingMiddleware)

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

def gemini_chat(prompt, texto_pdf=None):
    """
    Função simulada de chamada à IA.
    Substitua pelo seu código real de integração com Gemini, GPT, etc.
    """
    if texto_pdf:
        # Aqui você pode montar o prompt para a IA usando o texto do PDF
        prompt_completo = f"{prompt}\n\nConteúdo do PDF:\n{texto_pdf[:2000]}"  # Limite para não enviar texto demais
        # Exemplo de resposta simulada:
        return f"Resumo gerado pela IA para o prompt: '{prompt}' com base no PDF: {texto_pdf[:300]}..."
    else:
        # Exemplo de resposta simulada só com o prompt
        return f"Resposta da IA para o prompt: '{prompt}'"

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

@app.post("/chat/pdf")
async def chat(
    request: Request,
    prompt: str = Form(None),
    pdf: UploadFile = None
):
    # Tenta pegar o prompt do form-data
    if prompt is not None:
        prompt_text = prompt
    else:
        # Se não veio via form, tenta pegar do JSON
        data = await request.json()
        prompt_text = data.get("prompt")

    texto_pdf = ""
    if pdf is not None:
        reader = PyPDF2.PdfReader(pdf.file)
        for page in reader.pages:
            texto_pdf += page.extract_text() or ""
        response_text = gemini_chat(prompt_text, texto_pdf)
    else:
        response_text = gemini_chat(prompt_text)

    return JSONResponse(content={"response": response_text})

@app.get("/logs")
async def get_logs():
    """Retorna todos os logs de requisição da sessão"""
    return {"total_requests": len(request_logs), "logs": request_logs}