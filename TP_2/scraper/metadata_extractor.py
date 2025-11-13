"""
Extracción de metadatos (meta tags) desde un objeto BeautifulSoup.
"""

from typing import Dict

from bs4 import BeautifulSoup


def extract_meta_tags(soup: BeautifulSoup) -> Dict[str, str]:
    """
    Extrae meta tags relevantes:
      - description
      - keywords
      - og:* (Open Graph)

    Devuelve un dict {nombre: valor}
    """
    meta_tags: Dict[str, str] = {}

    for meta in soup.find_all("meta"):
        name = meta.get("name") or meta.get("property")
        if not name:
            continue

        name = name.lower()
        if name in ("description", "keywords") or name.startswith("og:"):
            meta_tags[name] = meta.get("content", "") or ""

    return meta_tags
