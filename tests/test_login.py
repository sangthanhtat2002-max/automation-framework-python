from pages.login_page import LoginPage
import pytest   

def test_login_success(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_success()

def test_login_fail(login_page):
    with pytest.raises(ValueError):
        login_page.login("", "123")