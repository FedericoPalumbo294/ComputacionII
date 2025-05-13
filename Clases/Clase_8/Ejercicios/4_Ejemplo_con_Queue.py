# Una Queue (cola) permite que múltiples procesos pongan y saquen datos de forma segura.
# Es útil cuando muchos hijos necesitan comunicarse con el padre.
# En este ejemplo, el proceso hijo envía números al padre a través de una Queue.

from multiprocessing import Process, Queue

def cuadrado(numeros, cola):
    print("Soy el proceso hijo y los numeros son:", numeros) # Aca imprimimos que somos el proceso hijo y los numeros que nos pasaron
    for n in numeros: # Aca dice que para cada numero en la lista de numeros se va a ejecutar el siguiente bloque de codigo
        cola.put(n * n) # Aca metemos el cuadrado de cada numero en la cola

if __name__ == '__main__':
    q = Queue()
    p = Process(target=cuadrado, args=([1, 2, 3], q)) # Aca creamos el proceso hijo y le pasamos la lista de numeros y la cola como argumentos
    p.start()
    p.join()
    print("Soy el proceso padre y los resultado que recivi son...") # Aca imprimimos que somos el proceso padre y los resultados que recibimos
    while not q.empty(): # Aca dice que mientras la cola(q) no este vacia se va a ejecutar el siguiente bloque de codigo
        print( q.get())
