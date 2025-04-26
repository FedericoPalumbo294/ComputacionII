import os
import time

def create_child(depth):
    if depth == 0:
        return

    pid = os.fork()
    if pid == 0:  # Código del hijo
        time.sleep(1) # Espera de 1 segundo
        print(f"Soy el hijo de nivel {depth}, mi PID es {os.getpid()}, el PID de mi padre es {os.getppid()}") # Imprime el mensaje
        create_child(depth - 1) # Crea un hijo de nivel inferior
        os._exit(0)  # El hijo termina aquí
    else:  # Código del padre
        os.wait()  # El padre espera que su hijo termine antes de continuar

if __name__ == "__main__":# Código principal
    print(f"Soy el proceso principal, mi PID es {os.getpid()}")# Imprime el mensaje
    create_child(5)# Crea un hijo de nivel 5
    print("El proceso principal ha terminado.")# Imprime el mensaje
