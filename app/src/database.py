from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.src.config import DB_USER, DB_NAME, DB_PORT, DB_PASSWORD, DB_HOST, DB_PROVIDER

DB_URL = (
    f"{DB_PROVIDER}+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

Base = declarative_base()

engine = create_async_engine(DB_URL)


db_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with db_session() as session:
        yield session
