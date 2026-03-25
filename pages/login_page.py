from pages.base_page import BasePage
from config.config import BASE_URL
from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def open_login_page(self):
        self.open_url(BASE_URL)
    
    def enter_username(self, username):
        self.input_text(self.USERNAME, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def login(self, username, password):
        if not username or not password:
            raise ValueError("Missing username or password")

        logger.info("Start login flow")
        
        self.open_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_success(self):
        return "inventory" in self.driver.current_url
    
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def is_login_failed(self):
        try:
            return self.find(self.ERROR_MSG).is_displayed()
        except Exception:
            return False