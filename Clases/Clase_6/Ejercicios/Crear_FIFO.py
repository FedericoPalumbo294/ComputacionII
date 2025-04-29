# Para correr este código: 
# primero, desde una terminal, corremos el archivo crear-fifo.py
# Luego corremos el lector.py (Ahora en teoria se quedaría bloqueado, porque el fifo está vacío)
# Y luego, en otra terminal, corremos el archivo escritor.py.
# Después de hacer eso, en la primera terminal, ya el lector se desbloquearia y leeria el mensaje

import os

fifo_path = "/tmp/mi_fifo"

# Si ya existe, no lo volvemos a crear
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)
