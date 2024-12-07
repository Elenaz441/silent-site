from uuid import UUID

from fastapi_users import schemas
from pydantic import Field


class UserRead(schemas.BaseUser[UUID]):
    name: str = Field(min_length=2, max_length=32)


class UserCreate(schemas.BaseUserCreate):
    name: str = Field(min_length=2, max_length=32)


class UserUpdate(schemas.BaseUserUpdate):
    name: str = Field(min_length=2, max_length=32)
