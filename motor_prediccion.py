import pandas as pd
import os
import matplotlib
matplotlib.use('Agg') # <--- ESTA LÍNEA ES VITAL PARA SERVIDORES
import matplotlib.pyplot as plt
from datetime import import datetime

# =============================
# ARCHIVOS
# =============================
ARCHIVO_HISTORIAL = "historico_lottoactivo.xlsx"
ARCHIVO_PESOS = "pesos_animalitos.xlsx"

# =============================
# DATOS DE EJEMPLO (3 animalitos)
# =============================
predicciones = pd.DataFrame({
    "fecha_prediccion": [datetime.now().date()] * 3,
    "animalito": ["Perro", "Gato", "Caballo"],
    "frecuencia": [0.7, 0.7, 0.7]
})

# =============================
# HISTORIAL DE APRENDIZAJE
# =============================
if os.path.exists(ARCHIVO_HISTORIAL):
    df_historial = pd.read_excel(ARCHIVO_HISTORIAL)
else:
    print("📁 Archivo historial no existe, creando uno nuevo...")
    df_historial = pd.DataFrame(
        columns=["fecha_prediccion", "animalito", "frecuencia", "resultado"]
    )

nuevas_filas = []

for _, fila in predicciones.iterrows():
    nuevas_filas.append({
        "fecha_prediccion": fila["fecha_prediccion"],
        "animalito": fila["animalito"],
        "frecuencia": fila["frecuencia"],
        "resultado": "fallo"   # por ahora todos fallaron
    })

df_historial = pd.concat(
    [df_historial, pd.DataFrame(nuevas_filas)],
    ignore_index=True
)

df_historial.to_excel(ARCHIVO_HISTORIAL, index=False)

# =============================
# PESOS (APRENDIZAJE)
# =============================
if os.path.exists(ARCHIVO_PESOS):
    pesos = pd.read_excel(ARCHIVO_PESOS)
else:
    pesos = pd.DataFrame({
        "animalito": ["Perro", "Gato", "Caballo"],
        "peso": [1.0, 1.0, 1.0]
    })

for _, row in df_historial.iterrows():
    if row["resultado"] == "fallo":
        pesos.loc[pesos["animalito"] == row["animalito"], "peso"] *= 0.7

pesos.to_excel(ARCHIVO_PESOS, index=False)

# =============================
# MENSAJE FINAL
# =============================
print("✅ Predicción generada correctamente")
print("📉 Fallos registrados y aprendizaje aplicado")
print("🧠 Motor de predicción ejecutado con éxito")
# =============================
# 13. ALERTAS AUTOMATICAS
# =============================

ALERTA_ARCHIVO = "alertas_diarias.txt"

top_animales = pesos.sort_values("peso", ascending=False).head(3)

mensaje = "\nALERTA DE ANIMALITOS FUERTES\n"
mensaje += "---------------------------\n"

for _, row in top_animales.iterrows():
    mensaje += "Animal: " + str(row["animalito"]) + " | Peso: " + str(row["peso"]) + "\n"

print(mensaje)

with open(ALERTA_ARCHIVO, "a") as f:
    f.write("\n" + str(pd.Timestamp.now()) + "\n")
    f.write(mensaje)
# =============================
# 14. GRAFICO DE PESOS
# =============================

plt.figure()
plt.bar(pesos["animalito"], pesos["peso"])
plt.title("Peso de Animalitos")
plt.xlabel("Animalito")
plt.ylabel("Peso")
plt.show()
def ejecutar_prediccion():
    # aquí ya está toda tu lógica
    # solo devolvemos el resultado final

    predicciones = generar_predicciones()  # tu función existente

    salida = []
    for _, fila in predicciones.iterrows():
        salida.append({
            "animalito": fila["animalito"],
            "frecuencia": int(fila["frecuencia"])
        })

    return {
        "fecha": str(pd.Timestamp.now()),
        "top_3": salida
    }


