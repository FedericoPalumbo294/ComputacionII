# Objetivo:
# Realicen alguna tarea visible con sleep() y print()
# Usen multiprocessing.Process
# Demuestren que están corriendo en paralelo (no uno después del otro)


from multiprocessing import Process
from time import sleep, time

def tarea(nombre):
    print(f"Proceso {nombre} iniciando")
    sleep(2)
    print(f"Proceso {nombre} finalizó")

if __name__ == '__main__':
    inicio = time()
    
    procesos = []
    for i in range(4):  # Crear 4 procesos
        p = Process(target=tarea, args=(f"P{i+1}",))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    fin = time()
    print(f"Tiempo total: {fin - inicio:.2f} segundos")

