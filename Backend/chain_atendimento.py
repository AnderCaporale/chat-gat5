from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from operator import itemgetter

# Carregar as chaves APIs presentes no arquivo .env
load_dotenv()
# --------------------------------------------------------------------------------

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

## Contexto Recuperado:
<contexto>
</contexto>
"""

# Criando o ChatPromptTemplate com a entrada do usuário e o histórico:
atendimento_prompt_template = ChatPromptTemplate([("system", sys_atendimento_geral_prompt),
                                                  ("human", "Mensagem do usuário: {input_user}"),
                                                  ])

chain_de_atendimento_geral = (RunnableParallel({"input_user": itemgetter("input_user")
                                })
                                | atendimento_prompt_template
                                | modelo_groq
                                | StrOutputParser())
