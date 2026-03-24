from pages.base_page import BasePage
from config.config import BASE_URL

class LoginPage(BasePage):
    USERNAME_INPUT = "username_field"
    PASSWORD_INPUT = "password_field"
    LOGIN_BUTTON = "login_button"

    def open_page(self):
        self.open_url(BASE_URL)
    
    def enter_username(self, username):
        self.input_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        if not username or not password:
            raise ValueError("Missing username or password")
        
        self.open_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()