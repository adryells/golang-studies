import uvicorn
from fastapi import FastAPI

from apps.backend.app.routes.router import api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


uvicorn.run(app, host="0.0.0.0")
