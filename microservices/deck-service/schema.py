from pydantic import BaseModel
from uuid import UUID

class DictionaryAddDTO(BaseModel):
    name: str

class DictionaryDTO(DictionaryAddDTO):
    id: UUID

class DictionaryUpdateDTO(DictionaryAddDTO):
    name: str | None