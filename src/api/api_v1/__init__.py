from fastapi import APIRouter

from config import settings

from .room import router as room_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(room_router, prefix=settings.api.v1.rooms)
