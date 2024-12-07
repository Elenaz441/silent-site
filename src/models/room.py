from uuid import UUID, uuid4

import sqlalchemy as alchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Room(Base):
    __tablename__ = "room"

    id: Mapped[UUID] = mapped_column(alchemy.UUID, primary_key=True, default=uuid4)
    participant_name_1: Mapped[str] = mapped_column(String(length=32))
    participant_photo_1: Mapped[str] = mapped_column(String)
    participant_name_2: Mapped[str | None] = mapped_column(String(length=32))
    participant_photo_2: Mapped[str | None] = mapped_column(String)
    is_waiting: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"
