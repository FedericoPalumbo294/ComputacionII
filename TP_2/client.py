#!/usr/bin/env python3
"""
Cliente simple para probar el Servidor A (Scraping).
Permite:
- ingresar una URL o recibirla por argumento
- realizar la petición HTTP al servidor A
- mostrar un resumen de los datos
- guardar el screenshot (si existe) como screenshot.png
"""

import sys
import base64
import asyncio
import aiohttp


SERVER_URL = "http://127.0.0.1:8000/scrape?url="


async def fetch_result(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(SERVER_URL + url) as resp:
            resp.raise_for_status()
            return await resp.json()


def save_screenshot(b64_data: str, filename="screenshot.png"):
    if not b64_data:
        print("No se recibió screenshot.")
        return

    try:
        data = base64.b64decode(b64_data)
        with open(filename, "wb") as f:
            f.write(data)
        print(f"Screenshot guardado como {filename}")
    except Exception as e:
        print(f"No se pudo guardar screenshot: {e}")


async def main():
    # Si la URL viene por argumento:
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        url = input("Ingrese URL a analizar: ").strip()

    print(f"Consultando al servidor por: {url}\n")

    try:
        result = await fetch_result(url)
    except Exception as e:
        print(f"Error al comunicarse con el servidor A: {e}")
        return

    scraping = result.get("scraping_data", {})
    processing = result.get("processing_data", {})

    print("=== SCRAPING DATA ===")
    print(f"Título: {scraping.get('title')}")
    print(f"Links encontrados: {len(scraping.get('links', []))}")
    print(f"Cantidad de imágenes: {scraping.get('images_count')}")
    print("Headers encontrados:")
    for k, v in scraping.get("structure", {}).items():
        print(f"  {k}: {v}")

    if scraping.get("meta_tags"):
        print("\nMeta Tags relevantes:")
        for k, v in scraping["meta_tags"].items():
            print(f"  {k}: {v}")

    print("\n=== PROCESSING DATA ===")
    if processing:
        perf = processing.get("performance", {})
        print(f"Tiempo de carga (ms): {perf.get('load_time_ms')}")
        print(f"Tamaño total (KB): {perf.get('total_size_kb')}")
        print(f"Cantidad requests: {perf.get('num_requests')}")
    else:
        print("No se recibió procesamiento. (Servidor B puede estar apagado)")

    # Guardar screenshot si existe
    if processing and "screenshot" in processing:
        save_screenshot(processing["screenshot"])
    else:
        print("No hay screenshot para guardar.")

    # Thumbnails
    thumbs = processing.get("thumbnails", []) if processing else []
    if thumbs:
        print(f"\nSe recibieron {len(thumbs)} thumbnails.")
        # Guardamos el primero:
        try:
            data = base64.b64decode(thumbs[0])
            with open("thumbnail.png", "wb") as f:
                f.write(data)
            print("Primer thumbnail guardado como thumbnail.png")
        except Exception:
            print("No se pudo guardar thumbnail.")


if __name__ == "__main__":
    asyncio.run(main())
    