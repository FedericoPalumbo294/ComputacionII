# En este ejercicio, el padre y el hijo se comunican a través de un pipe de cada hijo y el padre espera a que ambos hijos terminen.
# El hijo envía un mensaje al padre y el padre lo imprime en pantalla.

import os
import time

def crear_hijo(nombre):
    lectura, escritura = os.pipe()
    pid = os.fork()

    if pid == 0:
        # Código del hijo
        os.close(lectura)  # El hijo no va a leer

        print(f"[{nombre}] Empiezo mi tarea...")
        time.sleep(2)  # Simular trabajo

        mensaje = f"{nombre} ha terminado su tarea."
        os.write(escritura, mensaje.encode())
        os.close(escritura)
        os._exit(0)

    else:
        # Código del padre
        os.close(escritura)  # El padre no escribe

        recibido = os.read(lectura, 1024)
        print("[PADRE] Mensaje recibido:", recibido.decode())
        os.close(lectura)

        os.waitpid(pid, 0)  # Espera a que el hijo termine

def main():
    print("[PADRE] Comenzando la secuencia de procesos...")

    crear_hijo("Hijo A")
    crear_hijo("Hijo B")

    print("[PADRE] Ambos hijos terminaron. Fin del programa.")

if __name__ == "__main__":
    main()
