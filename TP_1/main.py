import time
import datetime
import random
from multiprocessing import Process, Pipe, Queue
from analizadores import analizar
from verificador import verificador

def generar_dato():
    return {
        "timestamp": datetime.datetime.now().isoformat(timespec='seconds'),
        "frecuencia": random.randint(60, 180),
        "presion": [random.randint(110, 180), random.randint(70, 110)],
        "oxigeno": random.randint(90, 100)
    }

if __name__ == "__main__":
    # Pipes para enviar datos a analizadores
    parent_conn_A, child_conn_A = Pipe()
    parent_conn_B, child_conn_B = Pipe()
    parent_conn_C, child_conn_C = Pipe()

    # Queues para recibir resultados
    queue_A = Queue()
    queue_B = Queue()
    queue_C = Queue()

    # Lanzar procesos analizadores
    pA = Process(target=analizar, args=("frecuencia", child_conn_A, queue_A))
    pB = Process(target=analizar, args=("presion", child_conn_B, queue_B))
    pC = Process(target=analizar, args=("oxigeno", child_conn_C, queue_C))
    pA.start()
    pB.start()
    pC.start()

    # Lanzar proceso verificador
    pV = Process(target=verificador, args=(queue_A, queue_B, queue_C))
    pV.start()

    for _ in range(60):
        dato = generar_dato()
        parent_conn_A.send(dato)
        parent_conn_B.send(dato)
        parent_conn_C.send(dato)
        time.sleep(1)

    # Esperar finalización
    pA.join()
    pB.join()
    pC.join()
    pV.join()
