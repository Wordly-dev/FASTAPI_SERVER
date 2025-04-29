from uuid import UUID

from repository import DictionaryRepository
from shared import Service
from schema import DictionaryDTO

class DictionaryService(Service):
    repository = DictionaryRepository

    def __init__(self):
        super().__init__(self.repository)

    def get_many(self, *, where: dict | None = None, _ = None) -> list[DictionaryDTO]:
        result_orm = self.repository.get_many(where=where)
        return [DictionaryDTO.model_validate(row, from_attributes=True) for row in result_orm]

    def get_one(self, *, instance_id: UUID, _ = None) -> DictionaryDTO:
        result_orm = self.repository.get_one(instance_id=instance_id)
        return DictionaryDTO.model_validate(result_orm, from_attributes=True)

