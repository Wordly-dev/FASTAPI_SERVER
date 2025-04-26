from typing import Annotated

from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pydantic import Field
from uuid import UUID, uuid4

class Dictionary(Base):
    __tablename__ = "dictionaries"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    name: Mapped[Annotated[str, Field(min_length=2)]]
    words = relationship("Word", back_populates='dictionary', cascade="all, delete-orphan",
        passive_deletes=True)