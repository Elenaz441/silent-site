from typing import Optional
from uuid import UUID

from .base import PyBaseModel
from pydantic import Field


class RoomRead(PyBaseModel):
    id: UUID
    participant_name_1: str = Field(min_length=2, max_length=32)
    participant_photo_1: str = Field()
    participant_name_2: Optional[str] = Field(min_length=2, max_length=32)
    participant_photo_2: Optional[str] = Field()


class RoomCreate(PyBaseModel):
    participant_name_1: str = Field(min_length=2, max_length=32)
    participant_photo_1: str = Field()
