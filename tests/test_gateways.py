import pytest
from unittest.mock import AsyncMock
from source.gateways.solicitacao_exclusao_gateway import SolicitacaoExclusaoGateway

@pytest.mark.asyncio
async def test_salvar_solicitacao(mocker):
    mock_inserir_solicitacao_exclusao = mocker.patch("source.adapters.postgresql_adapter.inserir_solicitacao_exclusao", new_callable=AsyncMock)
    gateway = SolicitacaoExclusaoGateway()
    
    await gateway.salvar_solicitacao("Fulano", "Rua A 123", "123456789")
    
    mock_inserir_solicitacao_exclusao.assert_called_once_with("Fulano", "Rua A 123", "123456789")