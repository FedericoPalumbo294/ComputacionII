from collections import deque
import statistics

def analizar(tipo, conn, queue):
    ventana = deque(maxlen=30)
    while True:
        try:
            dato = conn.recv()
        except EOFError:
            break

        if tipo == "frecuencia":
            valor = dato["frecuencia"]
        elif tipo == "presion":
            valor = dato["presion"][0]  # Sistólica
        elif tipo == "oxigeno":
            valor = dato["oxigeno"]
        else:
            continue

        ventana.append(valor)
        media = statistics.mean(ventana)
        desv = statistics.stdev(ventana) if len(ventana) > 1 else 0

        resultado = {
            "tipo": tipo,
            "timestamp": dato["timestamp"],
            "media": media,
            "desv": desv
        }

        queue.put(resultado)
