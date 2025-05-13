# Ejemplo de uso de multiprocessing en Python
from multiprocessing import Process # aca importamos la clase Process que hara su trabajo como lo definimos en target e iniciara cuando llamemos a start
import os

# Definimos una función que será ejecutada en un proceso hijo
def tarea():
    print(f"Proceso hijo ejecutándose. PID: {os.getpid()}")


if __name__ == '__main__':
    print(f"Proceso principal. PID: {os.getpid()}")
    p = Process(target=tarea) # Crear un nuevo proceso (o sea el proceso hijo que ejecutará la función tarea)
    p.start() # Iniciar el proceso hijo (o sea ejecutar la función tarea en el proceso hijo)
    p.join() # Esperar a que el proceso hijo termine (o sea esperar a que la función tarea termine para que no sea un zombie o un proceso huérfano)
