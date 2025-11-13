#!/usr/bin/env python3
"""
Servidor de Procesamiento Distribuido (Parte B)

- Escucha en un puerto TCP.
- Recibe tareas desde el Servidor A (asyncio).
- Usa un Pool de multiprocessing para:
    - generar screenshots
    - analizar rendimiento
    - procesar imágenes (thumbnails)
- Devuelve un JSON serializado al Servidor A.

Protocolo:
    [4 bytes longitud N en big-endian] + [N bytes payload JSON]
"""

import argparse
from multiprocessing import Pool, cpu_count
import socketserver

from common.protocol import recv_message_sync, send_message_sync
from common.serialization import to_bytes, from_bytes

from processor import generate_screenshot, analyze_performance, process_images


def process_task(task: dict) -> dict:
    """
    Función que se ejecuta dentro del Pool de procesos.
    'task' es un dict recibido desde el Servidor A, por ejemplo:
        {"url": "https://example.com"}
    """
    url = task.get("url", "")

    screenshot_b64 = generate_screenshot(url)
    performance = analyze_performance(url)
    thumbnails = process_images(url)

    return {
        "screenshot": screenshot_b64,
        "performance": performance,
        "thumbnails": thumbnails,
    }


class ProcessingTCPHandler(socketserver.BaseRequestHandler):
    """
    Handler para cada conexión entrante.
    Usa el protocolo definido en common.protocol.
    """

    def handle(self):
        try:
            # Recibir mensaje del Servidor A (JSON serializado)
            payload = recv_message_sync(self.request)
            task = from_bytes(payload)

            # Enviar tarea al pool de procesos (bloqueante, pero en otro proceso)
            result = self.server.pool.apply(process_task, (task,))

            # Serializar resultado y enviarlo de vuelta
            response_bytes = to_bytes(result)
            send_message_sync(self.request, response_bytes)

        except Exception as e:
            # En caso de error, intentamos avisar algo al servidor A
            try:
                error_payload = to_bytes({"status": "error", "error": str(e)})
                send_message_sync(self.request, error_payload)
            except Exception:
                # Si ni siquiera podemos responder, simplemente cerramos
                pass


class ProcessingServer(socketserver.ThreadingTCPServer):
    """
    TCPServer que soporta múltiples conexiones concurrentes usando threads.
    Cada thread puede usar el Pool de procesos para CPU-bound.
    """
    allow_reuse_address = True

    def __init__(self, server_address, handler_class, pool: Pool):
        super().__init__(server_address, handler_class)
        self.pool = pool


def parse_args():
    parser = argparse.ArgumentParser(description="Servidor de Procesamiento Distribuido")
    parser.add_argument("-i", "--ip", required=True, help="Dirección de escucha")
    parser.add_argument("-p", "--port", required=True, type=int, help="Puerto de escucha")
    parser.add_argument(
        "-n",
        "--processes",
        type=int,
        default=cpu_count(),
        help="Número de procesos en el pool (default: CPU count)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    with Pool(processes=args.processes) as pool:
        with ProcessingServer((args.ip, args.port), ProcessingTCPHandler, pool) as server:
            print(f"[Processing] Escuchando en {args.ip}:{args.port} "
                  f"con {args.processes} procesos en el pool")
            server.serve_forever()


if __name__ == "__main__":
    main()
