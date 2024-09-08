from entities.solicitante import Solicitante
from gateways.solicitacao_exclusao_gateway import SolicitacaoExclusaoGateway

class ExclusaoDadosPessoaisUseCase:
    def __init__(self):
        self.gateway = SolicitacaoExclusaoGateway()

    async def executar(self, nome: str, endereco: str, telefone: str):
        solicitante = Solicitante(nome, endereco, telefone)
        await self.gateway.salvar_solicitacao(
            solicitante.nome, solicitante.endereco, solicitante.telefone
        )