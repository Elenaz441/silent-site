from uuid import UUID, uuid4

import sqlalchemy as alchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


class Room(Base):
    __tablename__ = "room"

    id: Mapped[UUID] = mapped_column(alchemy.UUID, primary_key=True, default=uuid4)

    user_list: Mapped[list['User']] = relationship(back_populates='room')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"
