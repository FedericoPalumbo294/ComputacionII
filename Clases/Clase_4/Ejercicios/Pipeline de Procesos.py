# Este script crea un pipeline de procesos en Python utilizando pipes anónimos.
# El padre crea dos hijos y se comunica con ellos a través de pipes.
# El padre envía un número al primer hijo, que lo multiplica y lo envía al segundo hijo.
# El segundo hijo devuelve el resultado al padre, que lo suma y lo imprime.
# El padre espera a que ambos hijos terminen antes de finalizar.

import os

def main():

    leer_pipe1, escribir_pipe1 = os.pipe()  # Creamos a pipe1 que usa Padre → Hijo1 
    leer_pipe2, escribir_pipe2 = os.pipe()  # Creamos a pipe2 que usa Hijo1 → Hijo2
    leer_pipe3, escribir_pipe3 = os.pipe()  # Creamos a pipe3 que usa Hijo2 → Padre

    pid = os.fork()
    # Código del Hijo 1
    if pid == 0:

        os.close(escribir_pipe1)  # Aca no vamos a escribir nada en el pipe 1 pero si leer

        os.close(leer_pipe2)  # Aca no vamos a leer nada del pipe 2 pero si escribir

        os.close(leer_pipe3)  # Cerrar el pipe de lectura
        os.close(escribir_pipe3)  # Cerrar el pipe de escritura
        # Aca no queremos leer ni escribir nada del pipe 3

        num = int(os.read(leer_pipe1, 10))  # Leer del pipe 1

        print(f"[Hijo 1] Paso {num} al Hijo 2")  # Imprimir el numero que leyo del pipe 1

        os.write(escribir_pipe2, str(num).encode())  # Escribir en el pipe 2

        os._exit(0)


    else:
        # Código del Hijo 2
        pid2 = os.fork()

        if pid2 == 0:

            os.close(leer_pipe1)  # Cerrar el pipe de lectura
            os.close(escribir_pipe1)  # Cerrar el pipe de escritura
            # Aca no queremos leer ni escribir nada del pipe 1

            os.close(escribir_pipe2)  # Aca no vamos a escribir nada en el pipe 2 pero si leer
            
            os.close(leer_pipe3)  # Aca no vamos a leer nada del pipe 3 pero si escribir

            num = int(os.read(leer_pipe2, 10))  # Leer del pipe 2

            num = num * num  # Multiplicar el numero que leyo del pipe 2

            print(f"[Hijo 2] Multiplico: {num}")  # Imprimir el numero que leyo del pipe 2

            os.write(escribir_pipe3, str(num).encode())  # Escribir en el pipe 3

            os._exit(0)

        # Código del Padre

        os.close(leer_pipe1)  # Aca no vamos a leer nada en el pipe 1 pero si escribir mas adelante

        os.close(leer_pipe2)  # Cerrar el pipe de lectura
        os.close(escribir_pipe2)  # Cerrar el pipe de escritura

        os.close(escribir_pipe3)  # Aca no vamos a escribir nada en el pipe 3 pero si leer

        numero = int(input("[Padre] Ingrese un número: "))  # Leer un numero del usuario

        os.write(escribir_pipe1, str(numero).encode())  # Escribir en el pipe 1

        resultado = int(os.read(leer_pipe3, 10))  # Leer del pipe 3

        print(f"[Padre] Resultado final (suma): {resultado + resultado}")  # Imprimir el resultado que leyo del pipe 3

        os.wait()
        os.wait()

if __name__ == "__main__":
    main()