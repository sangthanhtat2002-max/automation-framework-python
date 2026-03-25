import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def login_page():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield LoginPage(driver)
    
    driver.quit()