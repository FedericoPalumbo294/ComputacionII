"""
Módulo de scraping asíncrono.

Incluye:
- async_http: funciones para descargar HTML usando aiohttp
- html_parser: parsing de HTML y extracción de datos
- metadata_extractor: extracción de meta tags
"""

from .async_http import fetch_html, fetch_html_simple
from .html_parser import extract_scraping_data
from .metadata_extractor import extract_meta_tags
