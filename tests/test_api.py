import pytest
from core.constants import AccountType


def test_get_customer_accounts(accounts_client, demo_data):
    response = accounts_client.get_customer_accounts(demo_data.customer_id)
    assert response.status_code == 200
    assert "accounts" in response.json()

def test_create_account_type_checking(demo_data, accounts_client):
    response = accounts_client.create_account(
        customer_id = demo_data.customer_id,
        account_type = AccountType.CHECKING,
        initial_deposit = demo_data.ensure_account(AccountType.CHECKING)
    )
    assert response.status_code in [200, 201]
    assert "id" in response.json()

def test_create_transfer(demo_data, accounts_client):
    checking = demo_data.ensure_account(AccountType.CHECKING)
    savings = demo_data.ensure_account(AccountType.SAVINGS)

    response = accounts_client.create_transfer(
        from_account_id=checking,
        to_account_id=savings,
        amount=50.0
    )
    assert response.status_code == 200
    assert response.json().get("status") == "COMPLETED"