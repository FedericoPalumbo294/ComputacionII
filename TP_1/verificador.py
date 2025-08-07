import hashlib
import json
import os
from utils import calcular_hash

def verificador(queue_A, queue_B, queue_C):
    cadena = []
    if os.path.exists("blockchain.json"):
        with open("blockchain.json", "r") as f:
            cadena = json.load(f)

    for i in range(60):
        resultado_A = queue_A.get()
        resultado_B = queue_B.get()
        resultado_C = queue_C.get()

        datos = {
            resultado_A["tipo"]: {"media": resultado_A["media"], "desv": resultado_A["desv"]},
            resultado_B["tipo"]: {"media": resultado_B["media"], "desv": resultado_B["desv"]},
            resultado_C["tipo"]: {"media": resultado_C["media"], "desv": resultado_C["desv"]},
        }

        alerta = (
            datos["frecuencia"]["media"] >= 200 or
            datos["oxigeno"]["media"] < 90 or
            datos["presion"]["media"] >= 200
        )

        prev_hash = cadena[-1]["hash"] if cadena else "0"
        timestamp = resultado_A["timestamp"]

        bloque = {
            "timestamp": timestamp,
            "datos": datos,
            "alerta": alerta,
            "prev_hash": prev_hash,
        }

        bloque["hash"] = calcular_hash(bloque)

        cadena.append(bloque)

        print(f"Bloque {i+1} - Hash: {bloque['hash']} - Alerta: {bloque['alerta']}")

        with open("blockchain.json", "w") as f:
            json.dump(cadena, f, indent=2)
