from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db

app = FastAPI()


@app.get("/")
async def root(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("select 'API Lotto funcionando 🚀'"))
    return {"estado": result.scalar()}
