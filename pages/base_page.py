from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        logger.info(f"[ACTION] Open URL: {url}")

    def click(self, locator):
        try:
            logger.info(f"[ACTION] Click on {locator}")
        except Exception as e:
            logger.error(f"[ERROR] Cannot click {locator}: {e}")
            raise

    def input_text(self, locator, text):
        try:
            logger.info(f"[ACTION] Input '{text}' into {locator}")
        except Exception as e:
            logger.error(f"[ERROR] Cannot input {locator}: {e}")
            raise