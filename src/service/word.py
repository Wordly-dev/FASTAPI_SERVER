from sqlalchemy.orm import joinedload
from uuid import UUID

from models import Word
from repository import WordRepository
from schema import WordRelDTO
from utils import AbstractRepository
from utils.service import Service

class WordService(Service):
    repository: AbstractRepository = WordRepository

    def __init__(self):
        super().__init__(self.repository)

    def get_many(self, *, where: dict | None = None, _ = None) -> list[WordRelDTO]:
        result_orm = self.repository.get_many(where=where, options=[joinedload(Word.dictionary)])
        return [WordRelDTO.model_validate(row, from_attributes=True).model_dump(exclude={"dictionary_id"}) for row in result_orm]

    def get_one(self, *, instance_id: UUID, _ = None) -> WordRelDTO:
        result_orm = self.repository.get_one(instance_id=instance_id, options=[joinedload(Word.dictionary)])
        return WordRelDTO.model_validate(result_orm, from_attributes=True).model_dump(exclude={"dictionary_id"})
