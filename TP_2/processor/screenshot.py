import base64

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError:
    webdriver = None
    Options = None


def generate_screenshot(url: str) -> str:
    """
    Genera un screenshot en PNG de la página y lo devuelve en base64 (str).
    Si Selenium/ChromeDriver no están disponibles o algo falla, devuelve "".
    """
    if webdriver is None or Options is None:
        # Selenium no instalado: no rompemos el TP, solo devolvemos vacío
        return ""

    driver = None
    try:
        options = Options()
        # Modo headless (sin ventana)
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1280,720")

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # Si querés, acá podrías esperar un poco a que cargue el JS:
        # import time; time.sleep(2)

        png_bytes = driver.get_screenshot_as_png()
        return base64.b64encode(png_bytes).decode("ascii")

    except Exception:
        # Cualquier error: devolvemos string vacío
        return ""
    finally:
        if driver is not None:
            driver.quit()
