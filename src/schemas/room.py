from uuid import UUID

from .base import PyBaseModel
from .user import UserRead


class RoomRead(PyBaseModel):
    id: UUID
    users: list[UserRead]
