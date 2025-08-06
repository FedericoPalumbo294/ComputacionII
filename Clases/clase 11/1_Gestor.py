#!/usr/bin/env python3

##Correr en terminal##
# chmod +x gestor.py
# ./gestor.py --num 3 --verbose


import argparse
import os
import random
import time
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description="Crea procesos hijos que duermen un tiempo aleatorio")
    parser.add_argument('--num', type=int, required=True, help='Cantidad de procesos hijos a crear')
    parser.add_argument('--verbose', action='store_true', help='Activa mensajes detallados')
    args = parser.parse_args()

    print(f"[PADRE] PID del proceso padre: {os.getpid()}")

    hijos = []

    for i in range(args.num):
        pid = os.fork()
        if pid == 0:
            # Proceso hijo
            duracion = random.randint(1, 5)
            if args.verbose:
                print(f"[HIJO {os.getpid()}] Creado por {os.getppid()}, durmiendo {duracion} segundos...")
            time.sleep(duracion)
            if args.verbose:
                print(f"[HIJO {os.getpid()}] Finalizando.")
            os._exit(0)
        else:
            hijos.append(pid)

    # Espera a que todos los hijos terminen
    for pid in hijos:
        os.waitpid(pid, 0)

    print(f"[PADRE] Todos los hijos han finalizado.\n")
    print("[PADRE] Jerarquía de procesos:")
    subprocess.run(["pstree", "-p", str(os.getpid())])

if __name__ == "__main__":
    main()
