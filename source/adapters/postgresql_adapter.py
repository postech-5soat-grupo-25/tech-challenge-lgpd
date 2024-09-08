from databases import Database
import sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_DB=os.getenv("POSTGRES_DB")
POSTGRES_USER=os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD")
DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"

database = Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()

solicitacoes = sqlalchemy.Table(
    "solicitacoes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nome", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("endereco", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("telefone", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("tipo", sqlalchemy.String, nullable=False)
)

async def inserir_solicitacao_exclusao(nome: str, endereco: str, telefone: str):
    query = solicitacoes.insert().values(
        nome=nome, endereco=endereco, telefone=telefone, tipo="Exclusão de Dados Pessoais"
    )
    await database.execute(query)