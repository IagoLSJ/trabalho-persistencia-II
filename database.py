from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database
from Models import Base
import os
from dotenv import load_dotenv
import logging

load_dotenv("db.env")

def create_url_engine() ->str:
    try:
        POSTGRES_USER = os.getenv("POSTGRES_USER")
        POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
        POSTGRES_HOST = os.getenv("POSTGRES_HOST")
        POSTGRES_PORT = os.getenv("POSTGRES_PORT")
        POSTGRES_DB = os.getenv("POSTGRES_DB")
    except Exception as e:
        logging.error(f"Erro ao criar url de conexão ao banco de dados: {e}")
    
    POSTGRES_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    print(POSTGRES_URL)
    logging.info(f"Url de conexão ao banco de dados criada :{POSTGRES_URL}")
    return POSTGRES_URL

# Criar o motor do banco de dados
engine = create_engine(create_url_engine(), echo=False)

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


def main():
    init_database()


if __name__ == "__main__":
    main()

