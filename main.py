from http.client import HTTPException
import logging
from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager
from typing import List
from database import init_database, get_session
from Models import Evento, Organizador

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

class EventoCreate(BaseModel):
    nome: str
    data: str
    hora: str
    local: str
    capacidade: int
    organizador_id: int


class OrganizadorCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str


@app.get("/eventos", response_model=list[dict])
def listar_eventos(db: Session = Depends(get_session)):
    """
    Endpoint para listar todos os eventos.
    """
    eventos = db.query(Evento).all()
    if not eventos:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado.")
    return [
        {
            "id": evento.id,
            "nome": evento.nome,
            "data": evento.data,
            "hora": evento.hora,
            "local": evento.local,
            "capacidade": evento.capacidade,
            "organizador_id": evento.organizador_id
        }
        for evento in eventos
    ]

@app.post("/eventos", response_model=dict)
def criar_evento(evento: EventoCreate, db: Session = Depends(get_session)):
    """
    Endpoint para criar um novo evento.
    """
    # Verifica se o organizador existe
    organizador = db.query(Organizador).filter(Organizador.id == evento.organizador_id).first()
    if not organizador:
        raise HTTPException(
            status_code=400,
            detail="Organizador não encontrado. Por favor, forneça um organizador válido."
        )
    try:
        # Cria o novo evento
        novo_evento = Evento(
            nome=evento.nome,
            data=evento.data,
            hora=evento.hora,
            local=evento.local,
            capacidade=evento.capacidade,
            organizador_id=evento.organizador_id
        )
        db.add(novo_evento)
        db.commit()
        db.refresh(novo_evento)
        return {
            "id": novo_evento.id,
            "nome": novo_evento.nome,
            "data": novo_evento.data,
            "hora": novo_evento.hora,
            "local": novo_evento.local,
            "capacidade": novo_evento.capacidade,
            "organizador_id": novo_evento.organizador_id
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao criar o evento: {str(e)}"
        )
@app.post("/organizadores", response_model=dict)
def cadastrar_organizador(organizador: OrganizadorCreate, db: Session = Depends(get_session)):
    """
    Endpoint para cadastrar um novo organizador.
    """
    # Verifica se já existe um organizador com o mesmo email
    organizador_existente = db.query(Organizador).filter(Organizador.email == organizador.email).first()
    if organizador_existente:
        raise HTTPException(
            status_code=400,
            detail="Já existe um organizador cadastrado com este email."
        )

    try:
        # Cria um novo organizador
        novo_organizador = Organizador(
            nome=organizador.nome,
            email=organizador.email,
            telefone=organizador.telefone
        )
        db.add(novo_organizador)
        db.commit()
        db.refresh(novo_organizador)
        return {
            "id": novo_organizador.id,
            "nome": novo_organizador.nome,
            "email": novo_organizador.email,
            "telefone": novo_organizador.telefone
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao cadastrar o organizador: {str(e)}"
        )
