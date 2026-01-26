from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Date, Integer, String

class Base(DeclarativeBase):
    pass


class Sorteo(Base):
    __tablename__ = "sorteos"

    id: Mapped[int] = mapped_column(primary_key=True)
    fecha: Mapped[str] = mapped_column(Date)
    hora: Mapped[str] = mapped_column(String(10))
    animal: Mapped[str] = mapped_column(String(50))
    numero: Mapped[int]


class Prediccion(Base):
    __tablename__ = "predicciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    animal: Mapped[str] = mapped_column(String(50))
    probabilidad: Mapped[float]
