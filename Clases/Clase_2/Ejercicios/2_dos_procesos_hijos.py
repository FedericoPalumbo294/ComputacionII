# Crear dos procesos hijos, cada uno imprime algo distinto

import os

for i in range(2):
    pid = os.fork()
    if pid == 0:
        print(f"Hijo {i}: PID = {os.getpid()}")
        exit(0)

# Solo el padre ejecuta esto
for i in range(2):
    os.wait()
print("Padre: ambos hijos terminaron")
