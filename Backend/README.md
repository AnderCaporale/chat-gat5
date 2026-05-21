Criar o ambiente venv:
python -m venv venv     


Habilitar o ambiente venv:
venv\Scripts\activate    


Instalar as dependências (pip install):
langchain_groq
dotenv
fastapi
uvicorn


Criar arquivo .env com as API_KEYS:
GROQ_API_KEY="sua_key"


Rodar o arquivo server.py (trocar o PATH para o caminho que o projeto está):
c:\PATH\Projeto\Backend\venv\Scripts\python.exe c:/PATH/Projeto/Backend/server.py
