import json
from utils import calcular_hash

with open("blockchain.json", "r") as f:
    cadena = json.load(f)

corruptos = 0
alertas = 0
total = len(cadena)

for i in range(1, total):
    if cadena[i]["prev_hash"] != cadena[i-1]["hash"]:
        corruptos += 1
    if cadena[i]["hash"] != calcular_hash(cadena[i]):
        corruptos += 1
    if cadena[i]["alerta"]:
        alertas += 1

# Promedios
suma = {"frecuencia": 0, "presion": 0, "oxigeno": 0}
for b in cadena:
    suma["frecuencia"] += b["datos"]["frecuencia"]["media"]
    suma["presion"] += b["datos"]["presion"]["media"]
    suma["oxigeno"] += b["datos"]["oxigeno"]["media"]

with open("reporte.txt", "w") as r:
    r.write(f"Total de bloques: {total}\n")
    r.write(f"Bloques con alertas: {alertas}\n")
    r.write("Promedios generales:\n")
    r.write(f"- Frecuencia: {suma['frecuencia']/total:.2f}\n")
    r.write(f"- Presión: {suma['presion']/total:.2f}\n")
    r.write(f"- Oxígeno: {suma['oxigeno']/total:.2f}\n")
    r.write(f"Bloques corruptos: {corruptos}\n")

print("Verificación completa. Ver reporte.txt.")
