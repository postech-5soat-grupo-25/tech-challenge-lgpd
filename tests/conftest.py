import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from source.adapters.api_adapter  import routes

@pytest.fixture(scope="module")
def client():
    app = FastAPI()
    app.include_router(routes)
    return TestClient(app)