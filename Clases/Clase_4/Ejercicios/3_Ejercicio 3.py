# En este ejercicio, el padre y el hijo se comunican a través de un pipe.
# El hijo envía un mensaje al padre y el padre lo imprime en pantalla.

import os

def main():
    lectura, escritura = os.pipe()  # Creamos el pipe

    pid = os.fork()

    if pid == 0:
        # Código del Hijo
        os.close(lectura)  # El hijo no va a leer

        # Redirigimos la salida estándar (stdout) al pipe
        os.dup2(escritura, 1)  # stdout ahora escribe en el pipe
        os.close(escritura)

        # Ejecutar 'ls -l' reemplazando el proceso
        os.execlp("ls", "ls", "-l")

        # Nota: si exec() funciona, nada después de acá se ejecuta
    else:
        # Código del Padre
        os.close(escritura)  # El padre no escribe

        # Leemos toda la salida del hijo
        while True:
            datos = os.read(lectura, 1024)
            if not datos:
                break
            print(datos.decode(), end="")  # Mostrar lo que vino del hijo

        os.close(lectura)
        os.wait()

if __name__ == "__main__":
    main()
