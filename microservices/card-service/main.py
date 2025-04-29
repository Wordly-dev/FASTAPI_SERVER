from fastapi import FastAPI
import uvicorn

from router import router
from config import settings

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, settings.API_PORT)