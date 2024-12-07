from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from config import settings
from models import User
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import redis
import redis.asyncio


engine = create_async_engine(str(settings.db.url))
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_redis_async_session() -> AsyncGenerator[redis.Redis, None]:
    async with redis.asyncio.StrictRedis(host=settings.redis.host,
                                         port=settings.redis.port,
                                         password=settings.redis.password,
                                         decode_responses=True) as session:
        yield session


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)