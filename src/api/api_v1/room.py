from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from fastapi import APIRouter, Depends, status
from models import Room, User
from schemas import RoomRead, UserRead
from database import get_async_session

router = APIRouter(tags=["Room"])


@router.get("/", response_model=List[RoomRead])
async def get_rooms(db: AsyncSession = Depends(get_async_session)):
    stmt = (select(Room)
            .join(User)
            .group_by(Room.id)
            .having(func.count(User.id) == 1))
    result = await db.execute(stmt)
    room_models = result.scalars().all()
    rooms = []
    for room_model in room_models:
        stmt = select(User).where(User.room_id == room_model.id)
        result = await db.execute(stmt)
        user_models = result.scalars().all()
        users = [UserRead.model_validate(user) for user in user_models]
        room = RoomRead(id=room_model.id, users=users)
        rooms.append(room)
    return rooms


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_room(db: AsyncSession = Depends(get_async_session)):
    new_room = Room()
    db.add(new_room)
    await db.flush()
    await db.commit()
    return new_room.id



