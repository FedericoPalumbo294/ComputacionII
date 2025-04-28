# El padre crea un hijo y termina inmediatamente, mientras que el hijo espera a que el padre muera y se convierte en un proceso huérfano.
# El hijo imprime su PID y el PID de su nuevo padre (init). El padre termina rápidamente, lo que provoca que el hijo sea adoptado por init.

import os
import time

def main():
    pid = os.fork()

    if pid > 0:
        # Código del padre
        print(f"[PADRE] Soy el padre. Mi PID es {os.getpid()}. Crearé un hijo y terminaré inmediatamente.")
        os._exit(0)  # El padre termina rápido

    else:
        # Código del hijo
        print(f"[HIJO] Soy el hijo. Mi PID es {os.getpid()}.")
        print("[HIJO] Esperando 20 segundos para ser adoptado...")
        time.sleep(20)  # Espera a que el padre muera

        nuevo_ppid = os.getppid()
        print(f"[HIJO] Ahora mi nuevo padre (PPID) es {nuevo_ppid}.")
        print("[HIJO] Me quedo 20 segundos más para que puedas ver mi estado en 'ps'.")

        time.sleep(20)  # Tiempo suficiente para buscarlo en ps
        print("[HIJO] Terminando.")
        os._exit(0)

if __name__ == "__main__":
    main()

