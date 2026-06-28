from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from operator import itemgetter
from rag_Qdrant import conecta_banco_vetorial_pre_criado

# Carregar as chaves APIs presentes no arquivo .env
load_dotenv()
# --------------------------------------------------------------------------------

# Conecta Banco Vetorial
db_vetorial = conecta_banco_vetorial_pre_criado()
db_retriever = db_vetorial.as_retriever(search_kwargs={'k': 5})

"""Função para pegar o conteúdo de cada chunk e criar um unico texto/string"""
def cria_texto_dos_documentos_retornados(documentos):
    return "\n\n".join(doc.page_content for doc in documentos)

# Instanciar um chatmodel para comunicarmos com os modelos LLMs
modelo_groq = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

# Criando o ChatPromptTemplate que irá responder a pergunta usuário se estiver no escopo
sys_atendimento_geral_prompt = """ Você é um assistente de um hospital e tem como objetivo responder à perguntas dos
médicos. Os assuntos serão sobre dúvidas em relação à procedimentos hospitalares, cadastros e demais rotinas médicas.

## Regras:
1 - Nunca invente informação. Responda que desconhece o assunto se você não souber responder e diga para consultar o site
oficial da instituição.
2 - Sempre se baseie no contexto que é entregue entre as tags <contexto></contexto>. As informações presentes nestas tags
foram obtidas de uma base de conhecimento.
3 - Evite falar 'no contexto...' ou 'conforme o contexto...' porque o usuário desconheçe sobre a presença desse contexto.
4 - Escreva o texto em português simples. Não utilize sequências Unicode escapadas (como \u202f, \u00a0 ou \n).
5 - Use apenas caracteres Unicode normais e espaços comuns. Retorne o texto já renderizado, sem códigos de escape.


## Contexto Recuperado:
<contexto>
{contexto_obtido}
</contexto>
"""

def remover_unicode(texto):
    return texto.replace("\u202f", " ")

# Criando o ChatPromptTemplate com a entrada do usuário e o histórico:
atendimento_prompt_template = ChatPromptTemplate([("system", sys_atendimento_geral_prompt),
                                                  ("human", "Mensagem do usuário: {input_user}"),
                                                  ])

chain_de_atendimento_geral = (RunnableParallel({"input_user": itemgetter("input_user"),
                                                "contexto_obtido": itemgetter("input_user") | db_retriever | cria_texto_dos_documentos_retornados
                                       
                                })
                                | atendimento_prompt_template
                                | modelo_groq
                                | StrOutputParser()
                                | remover_unicode)
