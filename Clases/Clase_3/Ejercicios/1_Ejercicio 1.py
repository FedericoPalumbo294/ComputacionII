import os
import time
import multiprocessing

def hijo():
    print("[HIJO] Soy el hijo. Mi PID es:", os.getpid(), "Mi padre es:", os.getppid())
    time.sleep(4)  # Espera para que el padre vea primero el mensaje
    # El hijo crea un nieto (hijo del hijo)
    def nieto():
        print("[NIETO] ¡Nací!")
    
    # Crea el nieto
    proceso_nieto = multiprocessing.Process(target=nieto)
    proceso_nieto.start()
    proceso_nieto.join()  # Espera a que el nieto termine
    
    print("[HIJO] Nació un nuevo hijo, soy el padre del nieto.")
    time.sleep(2)  # Espera para que el padre vea que nació el nieto

def padre():
    print("[PADRE] Soy el padre. Mi PID es:", os.getpid())
    # Crear el hijo
    proceso_hijo = multiprocessing.Process(target=hijo)
    proceso_hijo.start()
    proceso_hijo.join()  # Espera a que el hijo termine

if __name__ == '__main__':
    padre()
