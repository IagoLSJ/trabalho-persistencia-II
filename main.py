import logging
from typing import List
from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel

from database import init_database  # Importa a inicialização do banco de dados



class Evento(BaseModel):
    qtd_pessoas: int
    local: str
    valor: str
    data: str
    organizadorId: int
    id: int

class Organizador(BaseModel):
    nome: str
    idade: int
    pix: str
    id: str
    eventos: List[Evento]


app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifecycle do FastAPI para verificar/criar o banco de dados ao iniciar a aplicação.
    """
    try:
        init_database()  # Inicializa o banco de dados e as tabelas
        yield
    except Exception as e:
        logging.error(f"Erro ao criar/verificar o banco de dados: {e}")
        raise

app = FastAPI(lifespan=lifespan)



