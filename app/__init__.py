from app.v1 import users
from fastapi import APIRouter

router = APIRouter()

router.include_router(users.router, prefix="/user", tags=['User'])
