"""
Módulo de procesamiento pesado (Servidor B).

Incluye:
- screenshot: generación de capturas de pantalla
- performance: análisis de rendimiento de carga
- image_processor: descarga y generación de thumbnails de imágenes
"""

from .screenshot import generate_screenshot
from .performance import analyze_performance
from .image_processor import process_images
