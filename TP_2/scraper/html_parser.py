"""
Funciones de parsing HTML usando BeautifulSoup.

Responsable de:
- crear el árbol de BeautifulSoup
- extraer título
- extraer links
- contar headers H1..H6
- contar imágenes
- integrar metadatos
"""

from typing import Dict, List

from bs4 import BeautifulSoup

from .metadata_extractor import extract_meta_tags


def _parse_html(html: str) -> BeautifulSoup:
    """
    Crea y devuelve un objeto BeautifulSoup a partir del HTML.
    Usa el parser 'lxml' (debes tenerlo instalado).
    """
    return BeautifulSoup(html, "lxml")


def _extract_title(soup: BeautifulSoup) -> str:
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    return ""


def _extract_links(soup: BeautifulSoup) -> List[str]:
    links: List[str] = []
    for a in soup.find_all("a", href=True):
        links.append(a["href"])
    return links


def _count_headers(soup: BeautifulSoup) -> Dict[str, int]:
    structure: Dict[str, int] = {}
    for i in range(1, 7):
        tag_name = f"h{i}"
        structure[tag_name] = len(soup.find_all(tag_name))
    return structure


def _count_images(soup: BeautifulSoup) -> int:
    return len(soup.find_all("img"))


def extract_scraping_data(html: str) -> Dict:
    """
    Punto de entrada principal para el servidor A.

    Recibe HTML bruto y devuelve un dict con:
      - title
      - links
      - meta_tags
      - structure (h1..h6)
      - images_count
    """
    soup = _parse_html(html)

    title = _extract_title(soup)
    links = _extract_links(soup)
    meta_tags = extract_meta_tags(soup)
    structure = _count_headers(soup)
    images_count = _count_images(soup)

    return {
        "title": title,
        "links": links,
        "meta_tags": meta_tags,
        "structure": structure,
        "images_count": images_count,
    }
