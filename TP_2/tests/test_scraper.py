import asyncio
import unittest

from scraper.async_http import fetch_html_simple
from scraper.html_parser import extract_scraping_data


TEST_URL = "https://example.com"


class TestScraper(unittest.TestCase):
    def test_fetch_and_parse_example_dot_com(self):
        # Descarga HTML de manera asíncrona
        html = asyncio.run(fetch_html_simple(TEST_URL))
        self.assertIsInstance(html, str)
        self.assertGreater(len(html), 0)

        # Extrae datos de scraping
        data = extract_scraping_data(html)

        # Verificamos estructura básica
        self.assertIn("title", data)
        self.assertIn("links", data)
        self.assertIn("meta_tags", data)
        self.assertIn("structure", data)
        self.assertIn("images_count", data)

        # Tipos básicos
        self.assertIsInstance(data["title"], str)
        self.assertIsInstance(data["links"], list)
        self.assertIsInstance(data["meta_tags"], dict)
        self.assertIsInstance(data["structure"], dict)
        self.assertIsInstance(data["images_count"], int)


if __name__ == "__main__":
    unittest.main()
