"""
Módulo común para utilidades compartidas entre los servidores y el cliente.

Re-exporta funciones útiles de:
- common.protocol
- common.serialization
"""

from .protocol import (
    FRAME_HEADER_SIZE,
    pack_message,
    unpack_message_length,
    recv_exact_sync,
    recv_message_sync,
    send_message_sync,
    recv_message_async,
    send_message_async,
)

from .serialization import (
    to_bytes,
    from_bytes,
)
