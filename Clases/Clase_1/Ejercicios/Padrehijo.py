import os
import time

def create_child(wait_time, message):
    pid = os.fork()
    if pid == 0:  # Código del hijo
        time.sleep(wait_time)
        print(f"{message}, mi PID es {os.getpid()}, el PID de mi padre es {os.getppid()}")
        os._exit(0)

if __name__ == "__main__":
    create_child(0, "Soy el hijo 1")
    create_child(3, "Soy el hijo 2")
    
    time.sleep(1)
    print(f"Soy el padre, mi PID es {os.getpid()}")