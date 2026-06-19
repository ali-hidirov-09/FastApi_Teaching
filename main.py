from fastapi import FastAPI
from app import router


app = FastAPI(
    title="Teaching Project",
    description="BU mening o'quvchilarga dars berayotgan projectim",

)

app.include_router(router, prefix="/api/v1")

