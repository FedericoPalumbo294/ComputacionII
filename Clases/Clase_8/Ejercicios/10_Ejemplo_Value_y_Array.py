# La diferencia entre `Value` y `Array` es que `Value` se utiliza para compartir un solo valor entre procesos,
# mientras que `Array` se utiliza para compartir una colección de valores (como una lista o un array) entre procesos.
# Ambos son útiles para la comunicación entre procesos, pero se utilizan en diferentes situaciones según la necesidad 
# de compartir datos simples o estructuras de datos más complejas.

# En el ejemplo de "6_Ejemplo_sin_Lock.py" se utiliza `Value` para compartir un solo valor (la cuenta) entre dos procesos.
# Aca se muestra un ejemplo de cómo usar `Arrat` para compartir una lista de números entre procesos.

from multiprocessing import Process, Array

def duplicar(datos):
    for i in range(len(datos)):
        datos[i] *= 2

if __name__ == '__main__':
    numeros = Array('i', [1, 2, 3, 4])
    p = Process(target=duplicar, args=(numeros,))

    p.start()
    p.join()

    print(numeros[:])  # [2, 4, 6, 8]
