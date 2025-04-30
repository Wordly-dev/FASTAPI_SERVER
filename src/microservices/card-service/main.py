from fastapi import FastAPI
import uvicorn

import sys
from pathlib import Path

print(sys.path)
sys.path.append(str(Path(__file__).parent.parent.parent))
from router import router

print(sys.path)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app)