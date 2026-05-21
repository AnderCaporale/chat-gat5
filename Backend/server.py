import uvicorn
from fastapi import FastAPI, Request
from main import *
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:4200",  # Exemplo: seu frontend em localhost
    "*" # Permite todas as origens (não recomendado para produção)
]

app = FastAPI(title="Meu app")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    mensagem = body["input"]["input_user"]
    userId = body["config"]["id"]
    result = chain_principal.invoke({"input_user": mensagem}, config={"configurable": {"session_id": userId}})
    return result

uvicorn.run(app, host="localhost", port=8000)