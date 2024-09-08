from adapters.postgresql_adapter import inserir_solicitacao_exclusao

class SolicitacaoExclusaoGateway:
    async def salvar_solicitacao(self, nome: str, endereco: str, telefone: str):
        await inserir_solicitacao_exclusao(nome, endereco, telefone)