"""
Funciones de serialización/deserialización para mensajes entre servidores.

Por simplicidad, usamos JSON:
    - to_bytes(obj) -> bytes
    - from_bytes(bytes) -> objeto Python

Si en el futuro quisieras cambiar a pickle o protobuf, lo harías acá
y el resto del código seguiría igual.
"""

import json
from typing import Any


def to_bytes(obj: Any) -> bytes:
    """
    Serializa un objeto Python (tipicamente dict) a bytes usando JSON UTF-8.
    """
    text = json.dumps(obj, ensure_ascii=False)
    return text.encode("utf-8")


def from_bytes(data: bytes) -> Any:
    """
    Deserializa bytes (JSON UTF-8) a objeto Python.
    """
    text = data.decode("utf-8")
    return json.loads(text)
