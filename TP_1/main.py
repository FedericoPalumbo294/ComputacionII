import multiprocessing
import time
from datetime import datetime
import random
from analizador import proceso_analizador

def generar_muestra():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "frecuencia": random.randint(60, 180),
        "presion": [random.randint(110, 180), random.randint(70, 110)],
        "oxigeno": random.randint(90, 100)
    }

if __name__ == "__main__":
    # Crear pipes para los 3 analizadores
    parent_a, child_a = multiprocessing.Pipe()
    parent_b, child_b = multiprocessing.Pipe()
    parent_c, child_c = multiprocessing.Pipe()

    # Crear procesos analistas
    proc_a = multiprocessing.Process(target=proceso_analizador, args=(child_a, "frecuencia"))
    proc_b = multiprocessing.Process(target=proceso_analizador, args=(child_b, "presion"))
    proc_c = multiprocessing.Process(target=proceso_analizador, args=(child_c, "oxigeno"))

    # Iniciar procesos
    proc_a.start()
    proc_b.start()
    proc_c.start()

    for _ in range(60):
        muestra = generar_muestra()
        print(f"[Principal] Generada muestra: {muestra}")

        parent_a.send(muestra)
        parent_b.send(muestra)
        parent_c.send(muestra)

        time.sleep(1)

    # Enviar señal de cierre
    parent_a.send("FIN")
    parent_b.send("FIN")
    parent_c.send("FIN")

    # Esperar a que terminen
    proc_a.join()
    proc_b.join()
    proc_c.join()

    print("[Principal] Finalizado.")
