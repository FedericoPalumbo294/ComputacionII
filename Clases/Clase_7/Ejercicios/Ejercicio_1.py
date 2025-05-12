#Ejemplo en Python (sólo observación de señal SIGINT)

import time

print("Presioná Ctrl+C para enviar SIGINT")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("¡Recibida señal SIGINT!")
