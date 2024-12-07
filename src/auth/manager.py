from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, InvalidPasswordException

from models import User
from schemas import UserCreate
from database import get_user_db
from config import settings
from uuid import UUID

SECRET = settings.auth.secret_key


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    # async def validate_password(
    #     self,
    #     password: str,
    #     user: Union[UserCreate, User],
    # ) -> None:
    #     if len(password) < 8:
    #         raise InvalidPasswordException(
    #             reason="Password should be at least 8 characters"
    #         )
    #     if user.email in password:
    #         raise InvalidPasswordException(
    #             reason="Password should not contain e-mail"
    #         )
    #     if user.name in password:
    #         raise InvalidPasswordException(
    #             reason="Password should not contain name"
    #         )


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
