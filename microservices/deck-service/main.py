from fastapi import FastAPI
from uuid import UUID
import uvicorn

from schema import DictionaryAddDTO, DictionaryUpdateDTO
from service import DictionaryService

app = FastAPI(prefix="/dictionaries", tags=["dictionaries"])
service = DictionaryService()

@app.get("/")
def get_many():
    return service.get_many()

@app.get("/{id}")
def get_one(id: UUID):
    return service.get_one(instance_id=id)

@app.post("/")
def create(data: DictionaryAddDTO):
    return service.create(instance_data=data)

@app.put("/{id}")
def update(id: UUID, data: DictionaryUpdateDTO):
    return service.update(instance_id=id, instance_data=data)

@app.delete("/{id}")
def delete(id: UUID):
    return service.delete(instance_id=id)

if __name__ == "__main__":
    uvicorn.run(app, port=8002)