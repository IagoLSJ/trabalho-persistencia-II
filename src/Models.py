from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Evento(Base):
    __tablename__ = "eventos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    data: Mapped[str] = mapped_column(nullable=False)
    hora: Mapped[str] = mapped_column(nullable=False)
    local: Mapped[str] = mapped_column(nullable=False)
    capacidade: Mapped[int] = mapped_column(nullable=False)
    organizador_id: Mapped[int] = mapped_column(ForeignKey("organizadores.id"), nullable=False)

    #Relações
    organizador: Mapped["Organizador"] = relationship(back_populates="eventos")
    participantes: Mapped[list["Participante"]] = relationship(back_populates="evento", cascade="all, delete-orphan")

class Organizador(Base):
    __tablename__ = "organizadores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    telefone: Mapped[str] = mapped_column(nullable=False)

    eventos: Mapped[list[Evento]] = relationship(back_populates="organizador")

class Participante(Base):
    __tablename__ = "participantes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    documento: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    telefone: Mapped[str] = mapped_column(nullable=False)
    ingresso: Mapped[str] = mapped_column(nullable=False)
    evento_id: Mapped[int] = mapped_column(ForeignKey("eventos.id"), nullable=False)

    evento: Mapped["Evento"] = relationship(back_populates="participantes")

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    tipo_servico: Mapped[str] = mapped_column(nullable=False)
    contato: Mapped[str] = mapped_column(nullable=False)
    telefone: Mapped[str] = mapped_column(nullable=False)
    contrato_evento_id: Mapped[int] = mapped_column(ForeignKey("eventos.id"), nullable=False)

    evento: Mapped["Evento"] = relationship(back_populates="fornecedores")

class Orçamento(Base):
    __tablename__ = "orcamentos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    valor_previsto: Mapped[float] = mapped_column(nullable=False)
    valor_gasto: Mapped[float] = mapped_column(nullable=False)
    categoria: Mapped[str] = mapped_column(nullable=False)
    forma_pagamento: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    evento_id: Mapped[int] = mapped_column(ForeignKey("eventos.id"), nullable=False)

    evento: Mapped["Evento"] = relationship(back_populates="orcamento")

# Adicionando os relacionamentos em eventos
Evento.fornecedores = relationship("Fornecedor", back_populates="evento", cascade="all, delete-orphan")
Evento.orcamento = relationship("Orçamento", back_populates="evento", uselist=False)
