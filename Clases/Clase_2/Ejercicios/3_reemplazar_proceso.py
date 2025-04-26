# Usar exec() para reemplazar un proceso

import os

pid = os.fork()

if pid == 0:
    print("Hijo: ejecutando `ls -l` con exec")
    os.execvp("ls", ["ls", "-l"])
else:
    os.wait()
    print("Padre: hijo terminó después de exec")
