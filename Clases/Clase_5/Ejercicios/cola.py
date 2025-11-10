from multiprocessing import Process, Queue

def productor(queue: Queue) -> None:
    """Envía pares 0..18 y una señal de fin."""
    for num in range(0, 20, 2):
        print(f"[Productor] Enviando: {num}")
        queue.put(num)
    queue.put("FIN")  # Señal de fin

def consumidor(queue: Queue) -> None:
    """Consume hasta recibir la señal de fin."""
    while True:
        item = queue.get()
        if item == "FIN":
            print("[Consumidor] Fin de la comunicación")
            break
        print(f"[Consumidor] Recibí {item} - Su doble es: {item * 2}")

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=productor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))
    p1.start(); p2.start()
    p1.join();  p2.join()
