# Simular un proceso zombi

import os
import time

pid = os.fork()

if pid == 0:
    print("Hijo: terminó")
    exit(0)
else:
    print("Padre: esperando 5 segundos sin hacer wait")
    time.sleep(5)
    os.wait()
    print("Padre: hijo recolectado")
