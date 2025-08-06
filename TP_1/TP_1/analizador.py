from collections import deque
import numpy as np

def proceso_analizador(pipe, tipo):
    ventana = deque(maxlen=30)

    while True:
        datos = pipe.recv()

        if datos == "FIN":
            print(f"[{tipo}] Proceso finalizado.")
            break

        valor = None
        if tipo == "frecuencia":
            valor = datos["frecuencia"]
        elif tipo == "presion":
            sistolica, diastolica = datos["presion"]
            valor = (sistolica + diastolica) / 2  # media de la tupla
        elif tipo == "oxigeno":
            valor = datos["oxigeno"]

        ventana.append(valor)

        if len(ventana) >= 2:
            media = np.mean(ventana)
            desv = np.std(ventana)
            print(f"[{tipo}] Media: {media:.2f} | Desv: {desv:.2f}")
        else:
            print(f"[{tipo}] Esperando llenar la ventana...")
