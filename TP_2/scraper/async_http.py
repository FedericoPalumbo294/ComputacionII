"""
Cliente HTTP asíncrono basado en aiohttp.

Responsable de:
- descargar HTML de una URL
- manejar timeouts y errores de red
"""

from typing import Optional

import aiohttp


DEFAULT_TIMEOUT = 30  # segundos


async def fetch_html(
    url: str,
    session: aiohttp.ClientSession,
    timeout: int = DEFAULT_TIMEOUT,
) -> str:
    """
    Descarga el HTML de una URL usando una sesión aiohttp ya creada.

    Levanta:
      - aiohttp.ClientError ante errores HTTP / red
      - asyncio.TimeoutError ante timeout
    """
    client_timeout = aiohttp.ClientTimeout(total=timeout)
    async with session.get(url, timeout=client_timeout) as resp:
        resp.raise_for_status()
        return await resp.text()


async def fetch_html_simple(url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """
    Versión simple: crea una sesión temporal, descarga HTML y la cierra.
    Útil para tests rápidos.
    """
    async with aiohttp.ClientSession() as session:
        return await fetch_html(url, session=session, timeout=timeout)
