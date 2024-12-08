from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import APIRouter, Depends, status
from models import Room
from schemas import RoomCreate, RoomRead
from database import get_async_session

router = APIRouter(tags=["Room"])


@router.get("/", response_model=List[RoomRead])
async def get_rooms(db: AsyncSession = Depends(get_async_session)):
    stmt = select(Room).where(Room.is_waiting == True)
    result = await db.execute(stmt)
    room_models = result.scalars().all()
    rooms = [RoomRead.model_validate(room_model) for room_model in room_models]
    return rooms


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_room(room: RoomCreate,
                      db: AsyncSession = Depends(get_async_session)):
    data = room.model_dump()
    new_room = Room(**data)

    db.add(new_room)
    await db.flush()
    await db.commit()
    return new_room.id



