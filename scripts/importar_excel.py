import pandas as pd
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL").replace("sslmode=require", "")

engine = create_async_engine(DATABASE_URL)


async def importar():

    df = pd.read_excel("historico.xlsx")

    async with engine.begin() as conn:
        for _, row in df.iterrows():
            await conn.execute(text("""
                INSERT INTO sorteos (fecha, hora, animal, numero)
                VALUES (:f, :h, :a, :n)
            """), {
                "f": row["fecha"],
                "h": row["hora"],
                "a": row["animal"],
                "n": row["numero"]
            })

    print("✅ Datos importados a Neon")


asyncio.run(importar())
