# Usa Telnet para conectarte manualmente a un servidor web en el puerto 80.
# Permite observar cómo responde un protocolo HTTP sin navegador.

# Comando a ejecutar en terminal (no dentro de Python):
# telnet example.com 80
# GET / HTTP/1.1
# Host: example.com
# (presionar Enter dos veces)

# En Python podés simular algo similar:
import socket

with socket.create_connection(("example.com", 80)) as s:
    s.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    print(s.recv(1024).decode())
