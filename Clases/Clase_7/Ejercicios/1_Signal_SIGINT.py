import signal
import time

# 1. Definimos una función handler
def mi_handler(sig, frame):
    print(f"\n→ Señal recibida: {sig}")
    print("Limpieza realizada. Finalizando el programa...")
    exit(0)

# 2. Asociamos SIGINT (Ctrl+C) al handler
signal.signal(signal.SIGINT, mi_handler)# Aca el programa asocia la señal al handler


# 3. Ejecutamos un bucle infinito
print("Ejecutando. Presioná Ctrl+C para detener.")
while True:
    time.sleep(5)
    print("Esperando...")