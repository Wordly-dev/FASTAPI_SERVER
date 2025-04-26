from fastapi import APIRouter
from uuid import UUID

from schema import WordAddDTO, WordUpdateDTO
from service import WordService

word_router = APIRouter(prefix="/words", tags=["words"])
service = WordService()

@word_router.get("/")
def get_many():
    return service.get_many()

@word_router.get("/{id}")
def get_one(id: UUID):
    return service.get_one(instance_id=id)

@word_router.post("/")
def create(data: WordAddDTO):
    return service.create(instance_data=data)

@word_router.put("/{id}")
def update(id: UUID, data: WordUpdateDTO):
    return service.update(instance_id=id, instance_data=data)

@word_router.delete("/{id}")
def deleteword(id: UUID):
    return service.delete(instance_id=id)