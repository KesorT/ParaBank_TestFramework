import pytest
from pages.login_page import LoginPage
from core.settings import settings 

@pytest.mark.ui
def test_login_success(page):
    # ARRANGE
    lp = LoginPage(page)
    username = settings.USERNAME
    password = settings.PASSWORD

    # ACT
    lp.open()
    lp.login(username, password)

    # ASSERT
    lp.assert_success()

@pytest.mark.ui
def test_login_invalid_credentials(page):
    # ARRANGE
    lp = LoginPage(page)
    invalid_username = "wrong_user"
    invalid_password = "wrong_pass"

    # ACT
    lp.open()
    lp.login(invalid_username, invalid_password)

    # ASSERT
    lp.assert_error()