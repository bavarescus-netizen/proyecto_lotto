from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db import get_db

router = APIRouter(prefix="/prediccion", tags=["Predicción"])


@router.get("/")
async def prediccion(db: AsyncSession = Depends(get_db)):

    query = text("""
        SELECT animal, COUNT(*) as freq
        FROM sorteos
        GROUP BY animal
        ORDER BY freq DESC
        LIMIT 3
    """)

    result = await db.execute(query)
    rows = result.fetchall()

    return [
        {"animal": r[0], "frecuencia": r[1]}
        for r in rows
    ]
