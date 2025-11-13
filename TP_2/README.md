# TP2 – Sistema de Scraping y Análisis Web Distribuido

Trabajo práctico de **Computación II**.  
El objetivo es implementar un sistema distribuido con dos servidores:

- **Servidor A**: servidor HTTP asíncrono (`asyncio + aiohttp`) que hace scraping.
- **Servidor B**: servidor de procesamiento (`multiprocessing + socketserver`) que realiza tareas pesadas.

El cliente solo habla con el Servidor A, que a su vez se comunica con el Servidor B por sockets.

---

## 1. Requisitos

- Python 3.12 (o 3.10+)
- Git
- Navegador web o `curl` para probar
- Opcional:
  - Chrome/Chromium + ChromeDriver (para screenshots reales con Selenium)

---

## 2. Estructura del proyecto

```text
TP_2/
├── common/
│   ├── __init__.py
│   ├── protocol.py          # Protocolo de comunicación (framing, header+payload)
│   └── serialization.py     # Serialización JSON ↔ bytes
├── processor/
│   ├── __init__.py
│   ├── screenshot.py        # Generación de screenshot (Selenium, base64)
│   ├── performance.py       # Análisis de rendimiento (tiempo, tamaño, requests)
│   └── image_processor.py   # Descarga imágenes y genera thumbnails (Pillow, base64)
├── scraper/
│   ├── __init__.py
│   ├── async_http.py        # Descarga HTML usando aiohttp (asíncrono)
│   ├── html_parser.py       # Parsing HTML, extracción de título, links, headers, etc.
│   └── metadata_extractor.py# Extracción de meta tags (description, keywords, og:*)
├── tests/
│   ├── test_scraper.py      # Tests del módulo scraper (pendiente)
│   └── test_processor.py    # Tests del módulo processor (pendiente)
├── client.py                 # Cliente de prueba (opcional)
├── server_scraping.py        # Servidor A: HTTP asíncrono
├── server_processing.py      # Servidor B: procesamiento paralelo
├── requirements.txt          # Dependencias del proyecto
└── README.md
