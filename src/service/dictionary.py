from uuid import UUID
from sqlalchemy.orm import selectinload

from repository import DictionaryRepository
from utils.service import Service
from schema import DictionaryRelDTO
from models import Dictionary, Word

class DictionaryService(Service):
    repository = DictionaryRepository

    def __init__(self):
        super().__init__(self.repository)

    def get_many(self, *, where: dict | None = None, _ = None) -> list[DictionaryRelDTO]:
        result_orm = self.repository.get_many(where=where, options=[selectinload(Dictionary.words).load_only(Word.id, Word.word, Word.translation)])
        return [DictionaryRelDTO.model_validate(row, from_attributes=True) for row in result_orm]

    def get_one(self, *, instance_id: UUID, _ = None) -> DictionaryRelDTO:
        result_orm = self.repository.get_one(instance_id=instance_id, options=[selectinload(Dictionary.words).load_only(Word.id, Word.word, Word.translation)])
        return DictionaryRelDTO.model_validate(result_orm, from_attributes=True)

