import os
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no configurada en Render")

# SQLAlchemy async necesita asyncpg
DATABASE_URL = DATABASE_URL.replace(
    "postgresql://",
    "postgresql+asyncpg://"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)


# Dependency para FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
