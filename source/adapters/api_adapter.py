from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from use_cases.exclusao_dados_pessoais_use_case import ExclusaoDadosPessoaisUseCase

routes = APIRouter()

class SolicitacaoInput(BaseModel):
    nome: str
    endereco: str
    telefone: str

@routes.post("/solicitacao/exclusao/")
async def criar_solicitacao_exclusao(solicitacao: SolicitacaoInput):
    use_case = ExclusaoDadosPessoaisUseCase()
    try:
        await use_case.executar(solicitacao.nome, solicitacao.endereco, solicitacao.telefone)
        return {"message": "Solicitação de exclusão de dados pessoais criada com sucesso!"}
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))