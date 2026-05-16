from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
import os

load_dotenv()

__llm = init_chat_model(
    model="llama-3.1-8b-instant", model_provider="groq", api_key=os.getenv("GROQ_API_KEY"), temperature=0.7
)

app = FastAPI()

agent_cartao_credito = create_agent(
    __llm,
    tools=[],
    system_prompt=(
        "Você é um especialista em cartão de crédito do banco MDBank. "
        "Ajude o cliente com dúvidas, solicitação e limites."
    )
)

class AbrirContaRequest(BaseModel):
    message: str


@app.post("/send")
async def consultar(request: AbrirContaRequest):
    mensagem = request.message
    if not mensagem:
        raise HTTPException(
            status_code=400, detail="Campo 'message' obrigatório"
        )
    
    try:
        resultado = agent_cartao_credito.invoke(
            {"messages": [HumanMessage(content=mensagem)]}
        )
        mensagem_ia = resultado["messages"][-1]
        return {"resposta": mensagem_ia.content}
    except Exception as e:
        raise HTTPException(status_code=500,  detail=str(e))
    
@app.get("/")
async def health():
    return {"status": "ok"}