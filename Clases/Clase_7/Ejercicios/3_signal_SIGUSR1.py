import signal
import time
import os

# Mostramos el PID del proceso
print(f"PID del proceso: {os.getpid()}")

# Guardamos el tiempo actual
tiempo_actual = time.time()

# 1. Definimos un handler para SIGUSR1
def manejar_sigusr1(sig, frame):
    print("¡SIGUSR1 recibida! Guardando datos...")
    exit (0)

# 2. Asociamos SIGUSR1 (kill -10 <PID>) al handler
signal.signal(signal.SIGUSR1, manejar_sigusr1)

print("Esperando la señal SIGUSR1 (por defecto no hace nada si no se especifica un handler)...")

# 3. Bucle infinito para mantener el proceso vivo
while True:
    time.sleep(5)
    print("El proceso está activo, esperando señales...")

    if time.time() - tiempo_actual >= 30:
            print("⏳ Tiempo agotado. Finalizando el programa automáticamente.")
            exit(0)