from contextlib import asynccontextmanager
from fastapi import FastAPI
from .controllers import post, authentication
from .database import database, engine, metadata

metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {
        "message": "DIO Blog API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(authentication.router)
app.include_router(post.router)
