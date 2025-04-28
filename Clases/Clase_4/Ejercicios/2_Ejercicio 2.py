# En este ejercicio, el padre y el hijo se comunican a través de un pipe de cada hijo y el padre espera a que ambos hijos terminen.

import os

def crear_hijo(nombre):
    lectura, escritura = os.pipe()
    pid = os.fork()

    if pid == 0:
        # Código del Hijo
        os.close(lectura)  # Cierra lectura, solo escribirá
        mensaje = f"Hola, soy {nombre}!"
        os.write(escritura, mensaje.encode())
        os.close(escritura)
        os._exit(0)

    else:
        # Código del Padre
        os.close(escritura)  # Cierra escritura, solo leerá
        recibido = os.read(lectura, 1024)
        print(f"[PADRE] Recibí del {nombre}:", recibido.decode())
        os.close(lectura)
        os.waitpid(pid, 0)  # Espera a que ese hijo termine

def main():
    print("[PADRE] Comenzando la doble bifurcación...")

    crear_hijo("Hijo A")
    crear_hijo("Hijo B")

    print("[PADRE] Ambos hijos terminaron. Fin del programa.")

if __name__ == "__main__":
    main()
