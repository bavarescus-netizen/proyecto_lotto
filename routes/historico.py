from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db import get_db

router = APIRouter(prefix="/historico", tags=["Histórico"])


@router.get("/")
async def historico(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT * FROM sorteos LIMIT 20"))
    rows = result.fetchall()

    return [dict(r._mapping) for r in rows]
