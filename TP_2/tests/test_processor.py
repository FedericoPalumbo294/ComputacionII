import unittest

from processor.performance import analyze_performance
from processor.image_processor import process_images

TEST_URL = "https://example.com"


class TestProcessor(unittest.TestCase):
    def test_analyze_performance(self):
        perf = analyze_performance(TEST_URL)

        # Debe tener estas claves
        self.assertIn("load_time_ms", perf)
        self.assertIn("total_size_kb", perf)
        self.assertIn("num_requests", perf)
        self.assertIn("status", perf)

        # Tipos básicos
        self.assertIsInstance(perf["load_time_ms"], int)
        self.assertIsInstance(perf["total_size_kb"], (int, float))
        self.assertIsInstance(perf["num_requests"], int)
        self.assertIsInstance(perf["status"], str)

    def test_process_images(self):
        thumbs = process_images(TEST_URL)

        # Siempre debería devolver una lista (aunque vacía)
        self.assertIsInstance(thumbs, list)
        for t in thumbs:
            self.assertIsInstance(t, str)
            # base64 normalmente no es vacío
            self.assertGreater(len(t), 0)


if __name__ == "__main__":
    unittest.main()
