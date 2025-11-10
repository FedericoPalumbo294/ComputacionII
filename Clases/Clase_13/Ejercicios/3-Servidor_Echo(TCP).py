## Descripción
# Este patrón reenvía al cliente exactamente lo que envía.
# Sirve para probar comunicación bidireccional y mantener sesiones abiertas.

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6000))
server.listen()
print("Servidor Echo escuchando en el puerto 6000...")

while True:
    conn, addr = server.accept()
    print("Cliente conectado:", addr)
    while data := conn.recv(1024):
        conn.sendall(data)
    conn.close()
