from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from fastapi import APIRouter, Depends, status, HTTPException
from models import User, Room
from schemas import UserRead, UserCreate
from database import get_async_session

router = APIRouter(tags=["User"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
        user: UserCreate,
        db: AsyncSession = Depends(get_async_session)
):
    stmt = select(Room).where(Room.id == user.room_id)
    result = await db.execute(stmt)
    if not result.scalar():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found"
        )
    data = user.model_dump()
    new_user = User(**data)
    db.add(new_user)
    await db.flush()
    await db.commit()
    return new_user.id


@router.get("/{user_id}", response_model=UserRead)
async def get_user(
        user_id: UUID,
        db: AsyncSession = Depends(get_async_session)
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return UserRead.model_validate(user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        user_id: UUID,
        db: AsyncSession = Depends(get_async_session)
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    room_id = user.room_id
    stmt = delete(User).where(User.id == user_id)
    await db.execute(stmt)
    await db.flush()

    stmt = select(User).where(Room.id == room_id)
    result = await db.execute(stmt)
    room_users = result.scalars().all()
    if len(room_users) == 0:
        stmt = delete(Room).where(Room.id == room_id)
        await db.execute(stmt)
        await db.flush()
    await db.commit()
