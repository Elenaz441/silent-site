from uuid import UUID, uuid4

import sqlalchemy as alchemy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Room


class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(alchemy.UUID, primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String(length=32))
    photo: Mapped[str] = mapped_column(String)
    room_id: Mapped[int] = mapped_column(ForeignKey(Room.id, ondelete='RESTRICT'), name='room')

    room: Mapped[Room] = relationship(back_populates='user_list')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"
