from pydantic import BaseModel
from uuid import UUID


class WordAddDTO(BaseModel):
    word: str
    translation: str
    dictionary_id: UUID

class WordUpdateDTO(BaseModel):
    word: str | None = None
    translation: str | None = None

class WordDTO(WordAddDTO):
    id: UUID

class WordNestedDTO(BaseModel):
    id: UUID
    word: str
    translation: str
    
class WordRelDTO(WordDTO):
    dictionary: "DictionaryDTO"