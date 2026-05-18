from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
import os

load_dotenv()

_llm = init_chat_model(
    model="llama-3.1-8b-instant", model_provider="groq", api_key=os.getenv("GROQ_API_KEY"), temperature=0.7
)

agente_cartoes = create_agent(
    _llm,
    tools=[],
    system_prompt=(
        "Você é um especialista em cartão de credito do banco MDBank. "
        "Segue os Tipos disponíveis de cartões: platinum, gold, silver, mdzao."
        "Quando o cliente solciitar um cartao do tipo platinum, você deve recomendar o cartão platinum, que tem os seguintes benefícios: [Hotel, Restaurante, pontos de cashback]"
        "Ajude o cliente com dúvidas, solicitação e limites"
    ),
)

async def run_agent(mensagem: str):
    resultado = agente_cartoes.invoke(
        {
            "messages": [HumanMessage(content=mensagem)]
        }
    )
    return resultado["messages"][-1].content