# Ejercicio 1: Crear un pipe entre padre e hijo
# En este ejercicio, el padre y el hijo se comunican a través de un pipe.
# El hijo envía un mensaje al padre y el padre lo imprime en pantalla.
import os

def main():
    lectura, escritura = os.pipe()  # Crear el pipe

    pid = os.fork()

    if pid == 0:
        # Hijo
        os.close(lectura)  # El hijo NO lee
        mensaje = "Hola padre, soy tu hijo! y te estoy mandando un mensaje"
        os.write(escritura, mensaje.encode())# Escribir en el pipe el "Mensaje"
        os.close(escritura)
        os._exit(0)# Terminar el proceso hijo (zombie)

    else:
        # Padre
        os.close(escritura)  # El padre NO escribe
        recibido = os.read(lectura, 1024)# Leer del pipe por completo, porque tiene como maximo 1024 bytes
        print("[PADRE] Mensaje recibido:", recibido.decode())
        os.close(lectura)
        os.wait()

if __name__ == "__main__":
    main()
