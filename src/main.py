from fastapi import FastAPI

from api import result_router

app = FastAPI()
app.include_router(prefix="/v1", router=result_router)