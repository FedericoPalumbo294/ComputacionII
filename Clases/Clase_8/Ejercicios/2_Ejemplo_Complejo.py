# En este ejemplo, creamos dos procesos que ejecutan la misma función.

from multiprocessing import Process
import os
import time

def saludar(nombre):
    print(f"Hola, soy {nombre}. Mi PID es {os.getpid()}")
    time.sleep(2)
    print(f"{nombre} terminó")

if __name__ == '__main__':
    print(f"PID principal: {os.getpid()}")
    p1 = Process(target=saludar, args=("Proceso 1",))
    p2 = Process(target=saludar, args=("Proceso 2",))

    p1.start()
    p2.start()

    print("Procesos iniciados...")

    print("¿p1 está vivo?", p1.is_alive())
    p1.join()
    p2.join()
    print("Todos los procesos han terminado.")
