from fastapi import FastAPI
import pandas as pd
from motor_prediccion import ejecutar_prediccion

app = FastAPI(title="API Lotto Activo")

@app.get("/")
def inicio():
    return {"estado": "API Lotto Activo funcionando correctamente"}

@app.get("/prediccion")
def obtener_prediccion():
    resultado = ejecutar_prediccion()
    return resultado
