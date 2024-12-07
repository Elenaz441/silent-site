from uuid import UUID
from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Depends
from models import User
from auth import (
    get_user_manager,
    auth_backend
)
from schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, UUID](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)

router = APIRouter(tags=["Auth"])

router.include_router(fastapi_users.get_auth_router(auth_backend))
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))


@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
