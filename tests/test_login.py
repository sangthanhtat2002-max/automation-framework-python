from pages.login_page import LoginPage
import pytest

def test_login_success(login_page):
    login_page.login("admin", "123")

def test_login_fail(login_page):
    with pytest.raises(ValueError):
        login_page.login("", "123")