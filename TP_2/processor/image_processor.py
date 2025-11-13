import base64
from io import BytesIO
from typing import List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from PIL import Image


def _download_html(url: str) -> str:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.text


def _extract_image_urls(html: str, base_url: str, max_images: int = 3) -> List[str]:
    soup = BeautifulSoup(html, "lxml")
    urls: List[str] = []

    for img in soup.find_all("img", src=True):
        src = img["src"]
        full_url = urljoin(base_url, src)
        urls.append(full_url)
        if len(urls) >= max_images:
            break

    return urls


def _download_image(url: str) -> bytes:
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    return resp.content


def _make_thumbnail(img_bytes: bytes, size=(200, 200)) -> bytes:
    with Image.open(BytesIO(img_bytes)) as img:
        img.thumbnail(size)
        out = BytesIO()
        img.save(out, format="PNG")
        return out.getvalue()


def process_images(url: str) -> List[str]:
    """
    Descarga el HTML de la página, busca algunas imágenes (<img>),
    genera thumbnails PNG (200x200) y devuelve una lista de strings base64.

    Si algo falla, devuelve [] o las que haya podido generar.
    """
    thumbnails_b64: List[str] = []

    try:
        html = _download_html(url)
    except Exception:
        return thumbnails_b64  # sin HTML no seguimos

    img_urls = _extract_image_urls(html, url, max_images=3)

    for img_url in img_urls:
        try:
            img_bytes = _download_image(img_url)
            thumb_bytes = _make_thumbnail(img_bytes)
            thumb_b64 = base64.b64encode(thumb_bytes).decode("ascii")
            thumbnails_b64.append(thumb_b64)
        except Exception:
            # ignoramos imágenes rotas / formatos raros
            continue

    return thumbnails_b64
