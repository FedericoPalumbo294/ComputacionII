import signal
import time
import os

# Mostramos el PID del proceso
print(f"PID del proceso: {os.getpid()}")

# 1. Definimos una función handler
def mi_handler(sig, frame):
    print(f"\n→ Señal recibida: {sig}")
    print("Limpieza realizada. Finalizando el programa...")
    exit(0)

# 2. Asociamos SIGTERM (kill <PID>) al handler
signal.signal(signal.SIGTERM, mi_handler)# Aca el programa asocia la señal al handler


# 3. Ejecutamos un bucle infinito
print("Ejecutando. Ve desde otra teminal y pon (kill <PID>) para detener.")
while True:
    time.sleep(5)
    print("Esperando...")
