#  Use apply_async() en vez de map()

from multiprocessing import Pool

def cuadrado(n):
    return n * n

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5]
    resultados = []

    with Pool(processes=4) as pool:
        for n in numeros:
            res = pool.apply_async(cuadrado, args=(n,)) # Aca usamos apply_async para aplicar la funcion cuadrado a cada numero en la lista numeros
            resultados.append(res) # Aca guardamos el resultado de cada tarea en la lista resultados

        resultados = [r.get() for r in resultados] # Aca usamos get() para obtener los resultados de cada tarea

    print(resultados)

# En este ejemplo, usamos `apply_async()` para aplicar la función `cuadrado` a cada número en la lista `numeros`.
# `apply_async()` permite enviar tareas a un grupo de procesos y obtener los resultados más tarde.
# Esto es útil cuando no sabemos cuántas tareas vamos a enviar de antemano o cuando queremos enviar tareas de forma dinámica.