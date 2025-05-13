from multiprocessing import Pool

def cuadrado(n):# Aca definimos la funcion cuadrado que recibe un numero n y devuelve el cuadrado de ese numero
    return n * n

if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5]

    with Pool(processes=4) as pool:# Aca creamos un Pool de procesos con 4 procesos
        resultados = pool.map(cuadrado, numeros)# Aca usamos el Pool para aplicar la funcion cuadrado a cada numero en la lista numeros

    print(resultados)
# En este ejemplo, usamos un Pool de procesos para calcular el cuadrado de una lista de números.
# El Pool gestiona un grupo de procesos y distribuye las tareas entre ellos(o sea cada proceso calcula el cuadrado de un número en paralelo).
# La función `map` aplica la función `cuadrado` a cada elemento de la lista `numeros` en paralelo.
