from fastapi import APIRouter
from uuid import UUID
import uvicorn

from schema import WordAddDTO, WordUpdateDTO
from service import WordService

app = APIRouter(prefix="/words", tags=["words"])
service = WordService()

@app.get("/")
def get_many():
    return service.get_many()

@app.get("/{id}")
def get_one(id: UUID):
    return service.get_one(instance_id=id)

@app.post("/")
def create(data: WordAddDTO):
    return service.create(instance_data=data)

@app.put("/{id}")
def update(id: UUID, data: WordUpdateDTO):
    return service.update(instance_id=id, instance_data=data)

@app.delete("/{id}")
def deleteword(id: UUID):
    return service.delete(instance_id=id)

if __name__ == "__main__":
    uvicorn.run(app, port=8003)