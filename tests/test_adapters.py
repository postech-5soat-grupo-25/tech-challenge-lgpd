import pytest
from fastapi.testclient import TestClient
from source.adapters.api_adapter import routes
from source.adapters.postgresql_adapter import inserir_solicitacao_exclusao


@pytest.fixture
def client():
    from fastapi import FastAPI
    app = FastAPI()
    app.include_router(routes)
    return TestClient(app)

def test_criar_solicitacao_exclusao(client):
    response = client.post("/solicitacao/exclusao/", json={
        "nome": "Fulano",
        "endereco": "Rua A 123",
        "telefone": "123456789"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Solicitação de exclusão de dados pessoais criada com sucesso!"}


@pytest.mark.asyncio
async def test_inserir_solicitacao_exclusao(mocker):
    mock_execute = mocker.patch("source.adapters.postgresql_adapter.database.execute", autospec=True)
    
    await inserir_solicitacao_exclusao("Fulano", "Rua A 123", "123456789")
    
    mock_execute.assert_called_once()
    args, kwargs = mock_execute.call_args
    assert args[0].startswith("INSERT INTO solicitacoes")
