
from multiprocessing import Process, Value
import time

def sumar(cuenta):
    for _ in range(100000):
        cuenta.value += 1

if __name__ == '__main__':
    cuenta = Value('i', 0)
    p1 = Process(target=sumar, args=(cuenta,))
    p2 = Process(target=sumar, args=(cuenta,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Cuenta final:", cuenta.value)
    
# En este ejemplo, dos procesos intentan incrementar la misma variable compartida sin usar un Lock.
# Esto puede causar condiciones de carrera, donde ambos procesos intentan modificar la variable al mismo tiempo.
# Al final, la cuenta puede no ser la esperada debido a la falta de sincronización.
# Para evitar esto, se recomienda usar un Lock o una Queue para asegurar que solo un proceso acceda a la variable compartida a la vez.
# En este caso, la cuenta final puede ser menor a 200000 debido a que ambos procesos intentan incrementar la misma variable al mismo tiempo.