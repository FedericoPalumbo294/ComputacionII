# Implementa un pequeño servidor TCP que escucha conexiones y un cliente que se conecta.
# Muestra cómo se envían y reciben bytes a través de un socket.

# Servidor
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)
print("Servidor esperando conexión...")

conn, addr = server.accept()
print("Conectado con:", addr)
msg = conn.recv(1024).decode()
print("Cliente dice:", msg)
conn.sendall(b"Hola cliente, mensaje recibido!")
conn.close()
server.close()

# Cliente
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))
client.sendall(b"Hola servidor!")
print(client.recv(1024).decode())
client.close()
