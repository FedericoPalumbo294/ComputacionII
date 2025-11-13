import time
from typing import Dict

import requests


def analyze_performance(url: str) -> Dict:
    """
    Mide:
      - tiempo de descarga del HTML principal (ms)
      - tamaño total descargado (KB)
      - número de requests (acá solo 1)
    Devuelve un dict apto para meter directo en el JSON final.
    """
    start = time.perf_counter()
    total_bytes = 0

    try:
        with requests.get(url, timeout=30, stream=True) as resp:
            resp.raise_for_status()
            for chunk in resp.iter_content(chunk_size=8192):
                if not chunk:
                    continue
                total_bytes += len(chunk)
    except Exception:
        duration_ms = int((time.perf_counter() - start) * 1000)
        return {
            "load_time_ms": duration_ms,
            "total_size_kb": 0,
            "num_requests": 0,
            "status": "error",
        }

    duration_ms = int((time.perf_counter() - start) * 1000)
    total_kb = round(total_bytes / 1024, 2)

    return {
        "load_time_ms": duration_ms,
        "total_size_kb": total_kb,
        "num_requests": 1,  # solo HTML principal
        "status": "ok",
    }
