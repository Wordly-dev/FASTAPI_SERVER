from fastapi import APIRouter
from uuid import UUID

from schema import DictionaryAddDTO, DictionaryUpdateDTO
from service import DictionaryService

dictionary_router = APIRouter(prefix="/dictionaries", tags=["dictionaries"])
service = DictionaryService()

@dictionary_router.get("/")
def get_many():
    return service.get_many()

@dictionary_router.get("/{id}")
def get_one(id: UUID):
    return service.get_one(instance_id=id)

@dictionary_router.post("/")
def create(data: DictionaryAddDTO):
    return service.create(instance_data=data)

@dictionary_router.put("/{id}")
def update(id: UUID, data: DictionaryUpdateDTO):
    return service.update(instance_id=id, instance_data=data)

@dictionary_router.delete("/{id}")
def delete(id: UUID):
    return service.delete(instance_id=id)