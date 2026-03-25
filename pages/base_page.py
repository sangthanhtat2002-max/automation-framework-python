from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        logger.info(f"Find element {locator}")
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        logger.info(f"Click on {locator}")
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def input_text(self, locator, text):
        logger.info(f"Input text {text} into {locator}")
        element = self.wait.until(
            EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def open_url(self, url):
        logger.info(f"Open URL {url}")
        self.driver.get(url)