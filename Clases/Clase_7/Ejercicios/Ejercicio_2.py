#Script en Python que ignora SIGINT

import signal
import time

# Definir un manejador que no hace nada
def ignorar_sigint(signum, frame):
    print(f"Se recibió SIGINT ({signum}), pero fue ignorada.")

# Asignar el manejador a SIGINT
signal.signal(signal.SIGINT, ignorar_sigint)

print("Ejecutando... (presioná Ctrl+C para intentar interrumpir)")
while True:
    time.sleep(1)


# 🧪 Probalo así:
# Guardá este archivo como ignorar_sigint.py.
# Ejecutalo: python3 ignorar_sigint.py
# Presioná Ctrl+C: verás el mensaje pero el programa sigue funcionando.