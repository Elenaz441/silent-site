from fastapi import APIRouter

from config import settings

from .room import router as room_router
from .user import router as user_router
from .websocket import router as websocket_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(room_router, prefix=settings.api.v1.rooms)
router.include_router(user_router, prefix=settings.api.v1.users)
router.include_router(websocket_router, prefix=settings.api.v1.websocket)
