from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database
from Models import Base
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Configurações do banco de dados
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "meu_banco")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Criar o motor do banco de dados
engine = create_engine(DATABASE_URL, echo=False)

# Configurar o SessionMaker
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_session() -> Session:
    return SessionLocal()

def init_database():
    """Inicializa o banco de dados e verifica/cria as tabelas."""
    if not database_exists(engine.url):
        create_database(engine.url)
        logging.info("Banco de dados criado com sucesso.")
    else:
        logging.info("Banco de dados já existe.")
    Base.metadata.create_all(bind=engine)
    logging.info("Tabelas verificadas/criadas com sucesso.")
