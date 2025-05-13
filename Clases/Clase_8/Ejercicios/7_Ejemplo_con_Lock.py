from multiprocessing import Process, Value, Lock

def sumar(cuenta, lock):
    for _ in range(100000):
        with lock:  # sección crítica
            cuenta.value += 1

if __name__ == '__main__':
    cuenta = Value('i', 0)
    lock = Lock()

    p1 = Process(target=sumar, args=(cuenta, lock))
    p2 = Process(target=sumar, args=(cuenta, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Cuenta final:", cuenta.value)
# En este ejemplo, usamos un Lock para asegurar que solo un proceso acceda a la variable compartida a la vez.
# Esto evita condiciones de carrera y asegura que la cuenta final sea la esperada (200000).