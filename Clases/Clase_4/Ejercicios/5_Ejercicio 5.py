# En este ejercicio, el padre y el hijo se comunican a través de un pipe.
# El hijo termina y se convierte en un proceso zombi.

import os
import time

def main():
    pid = os.fork()

    if pid == 0:
        # Código del hijo
        print("[HIJO] Terminé rápido y me voy a volver un zombi...")
        os._exit(0)

    else:
        # Código del padre
        print("[PADRE] Mi hijo terminó, pero voy a esperar 10 segundos antes de hacer wait().")
        print("[PADRE] Mientras tanto, podés abrir otra terminal y correr 'ps -el' para ver el zombi.")
        
        time.sleep(10)  # Espera sin hacer wait()

        print("[PADRE] Ahora sí, recojo a mi hijo.")
        os.waitpid(pid, 0)
        print("[PADRE] Hijo recogido, fin del programa.")

if __name__ == "__main__":
    main()
