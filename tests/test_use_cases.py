import pytest
from unittest.mock import AsyncMock
from source.use_cases.exclusao_dados_pessoais_use_case import ExclusaoDadosPessoaisUseCase

@pytest.mark.asyncio
async def test_executar(mocker):
    mock_salvar_solicitacao = mocker.patch("source.gateways.solicitacao_exclusao_gateway.SolicitacaoExclusaoGateway.salvar_solicitacao", new_callable=AsyncMock)
    use_case = ExclusaoDadosPessoaisUseCase()
    
    await use_case.executar("Fulano", "Rua A 123", "123456789")
    
    mock_salvar_solicitacao.assert_called_once_with("Fulano", "Rua A 123", "123456789")