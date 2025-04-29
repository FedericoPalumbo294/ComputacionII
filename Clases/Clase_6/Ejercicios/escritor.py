fifo_path = "/tmp/mi_fifo"

with open(fifo_path, "w") as fifo:
    fifo.write("Hola desde el escritor!\n")
