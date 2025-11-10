import os
import time

def crear_zombi():
    pid = os.fork()

    if pid == 0:
        # Proceso hijo: termina inmediatamente
        print(f"Hijo (PID: {os.getpid()}) finalizando...")
        os._exit(0)
    else:
        # Proceso padre: espera antes de recolectar al hijo
        print(f"Padre (PID: {os.getpid()}) creó al hijo (PID: {pid})")
        print("Esperando 10 segundos para que el hijo esté en estado zombi...")
        time.sleep(10)
        
        # Ahora recolecta el estado del hijo (evita que quede zombi permanente)
        os.waitpid(pid, 0)
        print("Estado del hijo recolectado. Fin del padre.")

if __name__ == "__main__":
    crear_zombi()
