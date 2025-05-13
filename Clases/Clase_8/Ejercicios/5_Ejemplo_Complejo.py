from multiprocessing import Process, Queue

def saludar(nombre, cola):
    cola.put(f"Hola soy {nombre}")

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=saludar, args=("Hijo 1", q))
    p2 = Process(target=saludar, args=("Hijo 2", q))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
    print("Todos los procesos han terminado.")
# En este ejemplo, creamos dos procesos que ejecutan la misma función y se comunican a través de una Queue.
# La función `saludar` toma un nombre y una cola como argumentos. Cada proceso hijo envía un saludo a la cola.
# Al final, el proceso padre imprime todos los saludos recibidos de los procesos hijos.