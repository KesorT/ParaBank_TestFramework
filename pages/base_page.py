from playwright.sync_api import Page, expect

from core.settings import settings

class BasePage:
    PATH = "/"
    def __init__(self, page: Page):
        self.page = page
    def open(self):
        url = f"{settings.BASE_URL.rstrip('/')}/{self.PATH.lstrip('/')}"
        self.page.goto(url)
    def should_have_url_part(self, part: str):
        expect(self.page).to_have_url(lambda u: part in u)
