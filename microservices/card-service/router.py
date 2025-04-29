from fastapi import APIRouter
from uuid import UUID

from services import CardService
from schemas import CardAddDTO, CardUpdateDTO

router = APIRouter()
card_service = CardService()

@router.get("/")
def get_many():
    return card_service.get_many()

@router.get("/{id}")
def get_one(id: UUID):
    return card_service.get_one(instance_id=id)

@router.post("/")
def create(data: CardAddDTO):
    return card_service.create(instance_data=data)

@router.put("/{id}")
def update(id: UUID, data: CardUpdateDTO):
    return card_service.update(instance_id=id, instance_data=data)

@router.delete("/{id}")
def delete(id: UUID):
    return card_service.delete(instance_id=id)