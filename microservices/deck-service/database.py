from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from pydantic import Field
from typing import Annotated
from uuid import UUID, uuid4

from config import settings


engine = create_engine(url=settings.SYNC_DB_URL)
session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Dictionary(Base):
    __tablename__ = "dictionaries"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    name: Mapped[Annotated[str, Field(min_length=2)]]