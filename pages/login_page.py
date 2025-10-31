from .base_page import BasePage
from playwright.sync_api import expect
import re

class LoginPage(BasePage):
    PATH = "/index.htm"

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    BTN_LOGIN = "input[value='Log In']"
    ERROR = ".error"

    def login(self, user: str, pwd: str):
        self.page.fill(self.USERNAME, user)
        self.page.fill(self.PASSWORD, pwd)
        self.page.click(self.BTN_LOGIN)

    def assert_success(self):
        expect(self.page).to_have_url(re.compile(r"/overview\.htm(?:[?#].*)?$"))

    def assert_error(self):
        expect(self.page.locator(self.ERROR)).to_be_visible()
