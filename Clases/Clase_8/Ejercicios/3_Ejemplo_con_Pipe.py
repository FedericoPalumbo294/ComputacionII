# Un Pipe crea un mensaje de dos vías entre dos procesos. Sirve para enviar y recibir datos.
# En este ejemplo, el proceso hijo envía un mensaje al proceso padre a través del Pipe.

from multiprocessing import Process, Pipe

def hijo(mensaje):
    mensaje.send("Hola desde el proceso hijo")
    mensaje.close()

if __name__ == '__main__':
    padre_msj, hijo_msj = Pipe()
    p = Process(target=hijo, args=(hijo_msj,))
    p.start()
    print("Padre recibió:", padre_msj.recv())
    p.join()
