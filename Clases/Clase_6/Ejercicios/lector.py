fifo_path = "/tmp/mi_fifo"

with open(fifo_path, "r") as fifo:
    contenido = fifo.read()
    print("Lector recibió:", contenido)
