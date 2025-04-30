from uuid import UUID

from repositories import CardRepository
from schemas import CardDTO
from shared import Service, AbstractRepository

class CardService(Service):
    repository: AbstractRepository = CardRepository

    def __init__(self):
        super().__init__(self.repository)

    def get_many(self, *, where: dict | None = None, _ = None) -> list[CardDTO]:
        result_orm = self.repository.get_many(where=where)
        return [CardDTO.model_validate(row, from_attributes=True).model_dump(exclude={"dictionary_id"}) for row in result_orm]

    def get_one(self, *, instance_id: UUID, _ = None) -> CardDTO:
        result_orm = self.repository.get_one(instance_id=instance_id)
        return CardDTO.model_validate(result_orm, from_attributes=True).model_dump(exclude={"dictionary_id"})
