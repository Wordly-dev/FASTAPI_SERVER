from pydantic import BaseModel
from uuid import UUID

class CardAddDTO(BaseModel):
    front_text: str
    back_text: str
    deck_id: UUID

class CardUpdateDTO(BaseModel):
    front_text: str | None = None
    back_text: str | None = None

class CardDTO(CardAddDTO):
    id: UUID