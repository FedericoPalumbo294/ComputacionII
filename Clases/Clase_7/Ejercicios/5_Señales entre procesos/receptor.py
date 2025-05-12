# Al correr este codigo  el programa sigue funcionando hasta que reciva SIGUSR1
# 🧪 Probalo así:
# Correr el archivo 5_receptor.py, luego correr el archivo 6_emisor.py dandole el PID del proceso receptor(del archivo 5_receptor.py)

import os
import signal
import time

# Script en Python que recibe SIGUSR1 y termina el proceso
def handler_usr1(sig, frame):
    print(f"Proceso {os.getpid()} recibió SIGUSR1")
    exit(0)

# 1. Definimos un handler para SIGUSR1
signal.signal(signal.SIGUSR1, handler_usr1)


# Mostramos el PID del proceso
print(f"Esperando señales... PID: {os.getpid()}")
while True:
    time.sleep(1)
