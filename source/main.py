from fastapi import FastAPI
from adapters.api_adapter import routes
from adapters.postgresql_adapter import database, solicitacoes
import sqlalchemy
from dotenv import load_dotenv


load_dotenv()

async def lifespan(app: FastAPI):
    await database.connect()
    engine = sqlalchemy.create_engine(str(database.url))
    solicitacoes.create(engine, checkfirst=True)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(routes)