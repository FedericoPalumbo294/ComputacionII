from multiprocessing import Process, Queue
import time
import random

def productor(queue: Queue, id_productor: int) -> None:
    """Cada productor envía 3 números aleatorios y al final una única señal FIN por sistema."""
    for _ in range(3):
        num = random.randint(1, 100)
        print(f"[Productor {id_productor}] Enviando: {num}")
        queue.put(num)
        time.sleep(random.random())
    # Nota: no enviamos FIN aquí para cada productor; lo gestiona el main.

def consumidor(queue: Queue, id_consumidor: int) -> None:
    """Cada consumidor procesa hasta recibir FIN."""
    while True:
        item = queue.get()
        if item == "FIN":
            print(f"[Consumidor {id_consumidor}] Terminando")
            # Reinyectar FIN para que otros consumidores también terminen
            queue.put("FIN")
            break
        print(f"[Consumidor {id_consumidor}] Recibí {item} - Doble: {item * 2}")

if __name__ == "__main__":
    random.seed(42)
    q = Queue()

    n_productores = 2
    n_consumidores = 2

    productores = [Process(target=productor, args=(q, i)) for i in range(n_productores)]
    consumidores = [Process(target=consumidor, args=(q, i)) for i in range(n_consumidores)]

    for p in productores + consumidores:
        p.start()

    # Cuando todos los productores terminan, inyectamos una única señal FIN
    for p in productores:
        p.join()
    q.put("FIN")

    for c in consumidores:
        c.join()
