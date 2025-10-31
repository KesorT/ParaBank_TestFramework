import pytest
from playwright.sync_api import sync_playwright
from core.settings import settings
from api.api_client import ApiClient
from core.account_manager import AccountManager

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=settings.HEADLESS, args=["--disable-dev-shm-usage"])
        yield browser
        browser.close()

@pytest.fixture()
def context(browser):
    context = browser.new_context(base_url=settings.BASE_URL, viewport={"width": 1366, "height": 825})
    yield context
    context.close()

@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def api():
    return ApiClient()

@pytest.fixture
def demo_user(api):
    manager = AccountManager(api)
    user = manager.ensure_user()
    checking = manager.ensure_account("CHECKING")
    savings = manager.ensure_account("SAVINGS")
    api.deposit(checking, 200.0)
    return {"user": user, "checking": checking, "savings": savings}