# Este ejemplo muestra cómo manejar señales en un programa multihilo.
# En este caso, se utiliza la señal SIGINT (Ctrl+C) para detener todos los hilos de manera segura.

import threading
import time
import os
import signal

# Variable compartida
detener_evento = threading.Event()

def handler(sig, frame):
    print("Señal recibida. Avisando a todos los hilos.")
    detener_evento.set()

def hilo_trabajador(nombre):
    while not detener_evento.is_set():
        print(f"{nombre} trabajando...")
        time.sleep(5)
    print(f"{nombre} terminando.")

# Registrar handler (solo posible en el hilo principal)
signal.signal(signal.SIGINT, handler)

# Crear hilos
t1 = threading.Thread(target=hilo_trabajador, args=("Hilo 1",))
t2 = threading.Thread(target=hilo_trabajador, args=("Hilo 2",))
t1.start()
t2.start()

print(f"PID: {os.getpid()} - Presioná Ctrl+C para detener.")
t1.join()
t2.join()
