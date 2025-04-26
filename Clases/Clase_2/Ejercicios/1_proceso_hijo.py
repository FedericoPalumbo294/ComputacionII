# Crear un proceso hijo que imprima su PID y luego termine

import os

pid = os.fork()

if pid == 0:
    print(f"Hijo: PID = {os.getpid()}")
else:
    os.wait()
    print(f"Padre: PID = {os.getpid()}, hijo terminado")
