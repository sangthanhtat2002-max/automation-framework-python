import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page():
    driver = "Chrome"
    return LoginPage(driver)