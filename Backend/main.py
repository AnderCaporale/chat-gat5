from langchain_core.runnables import RunnableParallel
from operator import itemgetter
from chain_atendimento import chain_de_atendimento_geral

chain_principal = (
    RunnableParallel({
        "input_user": itemgetter("input_user"),
    })
    | chain_de_atendimento_geral
)