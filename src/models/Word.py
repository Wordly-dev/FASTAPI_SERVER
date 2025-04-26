from typing import Annotated

from database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import Field
from uuid import UUID, uuid4

class Word(Base):
    __tablename__ = "words"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    word: Mapped[Annotated[str, Field(min_length=2)]]
    translation: Mapped[Annotated[str, Field(min_length=2)]]
    dictionary_id: Mapped[UUID] = mapped_column(ForeignKey("dictionaries.id", ondelete='CASCADE'))
    dictionary = relationship("Dictionary", back_populates="words")


