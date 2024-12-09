from uuid import UUID
from pydantic import Field

from .base import PyBaseModel


class UserRead(PyBaseModel):
    id: UUID
    name: str = Field(min_length=2, max_length=32)
    photo: str = Field()
    room_id: UUID


class UserCreate(PyBaseModel):
    name: str = Field(min_length=2, max_length=32)
    photo: str = Field()
    room_id: UUID
