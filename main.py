from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app import router
from exceptions import setup_exception_handlers
from core.database import engine, Base
import models
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield



app = FastAPI(
    title="Teaching Project",
    description="BU mening o'quvchilarga dars berayotgan projectim",
    lifespan=lifespan
)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')



setup_exception_handlers(app=app)
app.include_router(router, prefix="/api/v1")

