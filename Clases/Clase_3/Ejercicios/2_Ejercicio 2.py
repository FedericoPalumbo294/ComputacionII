import os
import time
import random

def corredor(nombre):
    print(f"[{nombre}] ¡Partí de la línea de salida!")
    tiempo_carrera = random.uniform(1.0, 5.0)  # Carrera entre 1 y 5 segundos
    time.sleep(tiempo_carrera)
    print(f"[{nombre}] ¡Llegué a la meta en {tiempo_carrera:.2f} segundos!")
    os._exit(0)

def carrera():
    corredores = ["Corredor 1", "Corredor 2", "Corredor 3"]
    procesos = {}

    print("[PADRE] Preparando la carrera...")

    for nombre in corredores:
        pid = os.fork()
        if pid == 0:
            corredor(nombre)
        else:
            procesos[pid] = nombre

    posiciones = []

    while procesos:
        pid_terminado, estado = os.wait()
        nombre = procesos.pop(pid_terminado)
        posiciones.append(nombre)
        print(f"[PADRE] {nombre} cruzó la meta!")

    print("\n🏆 Resultados de la carrera:")
    for i, nombre in enumerate(posiciones, start=1):
        print(f"  {i}° lugar: {nombre}")

if __name__ == "__main__":
    carrera()
