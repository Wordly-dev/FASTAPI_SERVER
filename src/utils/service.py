from uuid import UUID
from pydantic import BaseModel

from utils.repository import AbstractRepository

class Service:
    repository: AbstractRepository | None = None

    def __init__(self, repository: AbstractRepository):
        self.repository = repository()

    def get_many(self, *, where: dict | None = None, options: dict | None = None):
        return self.repository.get_many(where=where, options=options)

    def get_one(self, *, instance_id: UUID, options: dict | None = None):
        return self.repository.get_one(instance_id=instance_id, options=options)

    def create(self, *, instance_data: BaseModel):
        return self.repository.create(instance_data=instance_data.model_dump())

    def update(self, *, instance_id: UUID, instance_data: BaseModel):
        return self.repository.update(instance_id=instance_id, instance_data=instance_data.model_dump())

    def delete(self, *, instance_id: UUID):
        return self.repository.delete(instance_id=instance_id)
