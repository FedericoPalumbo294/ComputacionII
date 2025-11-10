## Descripción
# Construye manualmente una petición HTTP, enviando texto estructurado al servidor.
# Permite entender que un protocolo es solo texto con formato y encabezados.

import socket

host = "example.com"
port = 80
request = b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"

with socket.create_connection((host, port)) as s:
    s.sendall(request)
    response = s.recv(4096)
    print(response.decode(errors="ignore"))
