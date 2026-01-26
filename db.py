import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

# =============================
# DATABASE URL (Render / Neon)
# =============================
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no configurada")

# Neon necesita asyncpg
DATABASE_URL = DATABASE_URL.replace(
    "postgresql://",
    "postgresql+asyncpg://"
)

# =============================
# ENGINE
# =============================
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

# =============================
# SESSION MAKER
# =============================
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# =============================
# DEPENDENCY FASTAPI
# =============================
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
