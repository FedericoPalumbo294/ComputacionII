"""
Definición del protocolo de comunicación entre el Servidor de Scraping (A)
y el Servidor de Procesamiento (B).

Formato de mensaje:
    [4 bytes: longitud N en big-endian] + [N bytes: payload]

El payload es un bloque de bytes (por ejemplo, JSON serializado).
Acá solo nos encargamos de enmarcar (frame) / desenmarcar y de funciones
de envío/recepción síncronas y asíncronas.
"""

import asyncio
import struct
from typing import Optional

FRAME_HEADER_SIZE = 4  # bytes para la longitud


# ---------------------------
# Funciones de framing
# ---------------------------

def pack_message(payload: bytes) -> bytes:
    """
    Recibe un payload (bytes) y devuelve header + payload.
    Header: entero sin signo en big-endian con la longitud del payload.
    """
    header = struct.pack("!I", len(payload))
    return header + payload


def unpack_message_length(header: bytes) -> int:
    """
    Dado un header de 4 bytes, devuelve la longitud (int).
    """
    if len(header) != FRAME_HEADER_SIZE:
        raise ValueError("Header inválido: longitud incorrecta")
    (length,) = struct.unpack("!I", header)
    return length


# ---------------------------
# Modo síncrono (socket clásico)
# ---------------------------

def recv_exact_sync(sock, n: int) -> bytes:
    """
    Recibe exactamente n bytes desde un socket bloqueante.
    Lanza ConnectionError si la conexión se corta antes.
    """
    chunks = []
    total = 0
    while total < n:
        chunk = sock.recv(n - total)
        if not chunk:
            raise ConnectionError("Conexión cerrada mientras se recibían datos")
        chunks.append(chunk)
        total += len(chunk)
    return b"".join(chunks)


def recv_message_sync(sock) -> bytes:
    """
    Recibe un mensaje completo usando el protocolo (header + payload)
    desde un socket bloqueante.
    """
    header = recv_exact_sync(sock, FRAME_HEADER_SIZE)
    length = unpack_message_length(header)
    payload = recv_exact_sync(sock, length)
    return payload


def send_message_sync(sock, payload: bytes) -> None:
    """
    Envía un mensaje completo (header + payload) por un socket bloqueante.
    """
    framed = pack_message(payload)
    sock.sendall(framed)


# ---------------------------
# Modo asíncrono (asyncio streams)
# ---------------------------

async def recv_message_async(reader: asyncio.StreamReader) -> bytes:
    """
    Recibe un mensaje completo desde un StreamReader de asyncio
    usando el mismo protocolo (header + payload).
    """
    header = await reader.readexactly(FRAME_HEADER_SIZE)
    length = unpack_message_length(header)
    payload = await reader.readexactly(length)
    return payload


async def send_message_async(writer: asyncio.StreamWriter, payload: bytes) -> None:
    """
    Envía un mensaje completo (header + payload) usando StreamWriter de asyncio.
    """
    framed = pack_message(payload)
    writer.write(framed)
    await writer.drain()
