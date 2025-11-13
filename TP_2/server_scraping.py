#!/usr/bin/env python3
"""
Servidor de Scraping Web Asíncrono (Parte A)

- Expone un servidor HTTP (aiohttp) con endpoint:
    GET /scrape?url=...

- Para cada URL:
    1) Descarga HTML de forma asíncrona.
    2) Extrae:
        - título
        - links
        - meta tags
        - headers H1..H6
        - cantidad de imágenes
    3) Se comunica con el Servidor B (Processing) por socket TCP:
        - envía {"url": "..."}
        - recibe screenshot, performance, thumbnails
    4) Devuelve un JSON consolidado al cliente.
"""

import argparse
import asyncio
from datetime import datetime, timezone
from urllib.parse import urlparse

from aiohttp import web
import aiohttp

from common.protocol import send_message_async, recv_message_async
from common.serialization import to_bytes, from_bytes

from scraper.async_http import fetch_html
from scraper.html_parser import extract_scraping_data


# Config: dónde está corriendo el servidor de procesamiento (B)
PROCESSING_SERVER_IP = "127.0.0.1"
PROCESSING_SERVER_PORT = 9000


async def call_processing_server(url: str) -> dict:
    """
    Abre una conexión TCP con el Servidor B, envía una tarea {"url": ...}
    y espera la respuesta.
    Usa el protocolo asincrónico de common.protocol.
    """
    reader, writer = await asyncio.open_connection(
        PROCESSING_SERVER_IP, PROCESSING_SERVER_PORT
    )

    try:
        task = {"url": url}
        payload = to_bytes(task)
        await send_message_async(writer, payload)

        response_bytes = await recv_message_async(reader)
        response_obj = from_bytes(response_bytes)
        return response_obj
    finally:
        writer.close()
        await writer.wait_closed()


async def handle_scrape(request: web.Request) -> web.Response:
    """
    Handler para:
        GET /scrape?url=...
    """
    url = request.query.get("url")
    if not url:
        return web.json_response({"error": "Missing url parameter"}, status=400)

    parsed = urlparse(url)
    if not parsed.scheme:
        return web.json_response(
            {"error": "URL must include scheme (http/https)"},
            status=400,
        )

    # Descargar HTML asíncrono
    async with aiohttp.ClientSession() as session:
        try:
            html = await fetch_html(url, session=session)
        except asyncio.TimeoutError:
            return web.json_response(
                {"status": "failed", "error": "timeout while scraping"},
                status=504,
            )
        except aiohttp.ClientError as e:
            return web.json_response(
                {"status": "failed", "error": f"http error: {e}"},
                status=502,
            )

    # Extraer datos de scraping
    scraping_data = extract_scraping_data(html)

    # Llamar al servidor de procesamiento B
    try:
        processing_data = await call_processing_server(url)
        status = "success"
    except (ConnectionError, asyncio.TimeoutError, OSError) as e:
        # Si B falla, devolvemos al menos la parte de scraping
        processing_data = None
        status = "partial"

    # Armar respuesta final
    response_body = {
        "url": url,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "scraping_data": scraping_data,
        "processing_data": processing_data,
        "status": status,
    }

    return web.json_response(response_body)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Servidor de Scraping Web Asíncrono"
    )
    parser.add_argument("-i", "--ip", required=True, help="Dirección de escucha (IPv4/IPv6)")
    parser.add_argument("-p", "--port", required=True, type=int, help="Puerto de escucha")
    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=4,
        help="Número de workers (no estricto en asyncio, pero requerido por enunciado)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    app = web.Application()
    app.add_routes([web.get("/scrape", handle_scrape)])

    print(f"[Scraping] Escuchando en http://{args.ip}:{args.port}")
    web.run_app(app, host=args.ip, port=args.port)


if __name__ == "__main__":
    main()
