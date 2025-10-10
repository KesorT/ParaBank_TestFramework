import pytest, random, string
from api.api_client import ApiClient
from core.settings import settings
from core.account_manager import AccountManager
from core.utils import parse_response

@pytest.fixture(scope="session")
def accounts_client():
    return ApiClient()

@pytest.fixture(scope="session")
def customer_id_data(accounts_client):
    response = accounts_client.login(
        username=settings.USERNAME,
        password=settings.PASSWORD
    )
    assert response.status_code == 200
    customer_data = parse_response(response)
    customer_id = customer_data.get("customerId") or customer_data.get("id")
    assert customer_id is not None, "Login failed, customer ID not found"
    return customer_id

@pytest.fixture(scope="session")
def demo_data(accounts_client, customer_id_data):
    return AccountManager(accounts_client, customer_id_data)
