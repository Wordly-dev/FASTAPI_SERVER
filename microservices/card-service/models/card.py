from sqlalchemy.orm import Mapped, mapped_column
from pydantic import Field
from uuid import UUID, uuid4
from typing import Annotated

from database import Base

class Card(Base):
    __tablename__ = "cards"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())
    front_text: Mapped[Annotated[str, Field(min_length=1)]]
    back_text: Mapped[Annotated[str, Field(min_length=1)]]