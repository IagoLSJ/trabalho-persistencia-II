from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

class Base(DeclarativeBase):
    pass

class Evento(Base):
    __tablename__ = "eventos"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    qtd_pessoas: Mapped[int] = mapped_column(nullable=False)
    local: Mapped[str] = mapped_column(nullable=False)
    valor: Mapped[str] = mapped_column(nullable=False)
    data: Mapped[str] = mapped_column(nullable=False)
    organizador_id: Mapped[int] = mapped_column(ForeignKey("organizadores.id"), nullable=False)
    
    organizador: Mapped["Organizador"] = relationship(back_populates="eventos")

class Organizador(Base):
    __tablename__ = "organizadores"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    idade: Mapped[int] = mapped_column(nullable=False)
    pix: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    eventos: Mapped[list[Evento]] = relationship(back_populates="organizador")


