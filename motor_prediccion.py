import pandas as pd
import os
from datetime import datetime

ARCHIVO_HISTORIAL = "historico_lottoactivo.xlsx"


# ==========================================
# GENERAR PREDICCIONES (simple por ahora)
# ==========================================
def generar_predicciones():
    return [
        {"animal": "gallina", "peso": 0.7},
        {"animal": "jirafa", "peso": 0.7},
        {"animal": "pescado", "peso": 0.7},
    ]


# ==========================================
# MOTOR PRINCIPAL
# ==========================================
def ejecutar_prediccion():

    print("🔥 ejecutando prediccion...")

    predicciones = generar_predicciones()

    fecha = datetime.now().date()

    filas = []
    for p in predicciones:
        filas.append({
            "fecha_prediccion": fecha,
            "animalito": p["animal"],
            "frecuencia": p["peso"],
            "resultado": "pendiente"
        })

    df_nuevo = pd.DataFrame(filas)

    if os.path.exists(ARCHIVO_HISTORIAL):
        df_hist = pd.read_excel(ARCHIVO_HISTORIAL)
        df_hist = pd.concat([df_hist, df_nuevo], ignore_index=True)
    else:
        df_hist = df_nuevo

    df_hist.to_excel(ARCHIVO_HISTORIAL, index=False)

    return {"predicciones": predicciones}






