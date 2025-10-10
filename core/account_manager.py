from core.constants import AccountType
from core.balance_checker import AccountBalanceChecker

class AccountManager:
    def __init__(self, accounts_client, customer_id):
        self.accounts_client = accounts_client
        self.customer_id = customer_id
        self.balance_checker = AccountBalanceChecker(accounts_client)

    def _get_all_accounts(self):
        resp = self.accounts_client.get_customer_accounts(self.customer_id)
        resp.raise_for_status()
        return resp.json().get("accounts", [])

    def ensure_account(self, account_type: AccountType):
        accounts = self._get_all_accounts()
        target = next((a for a in accounts if a["type"] == account_type.name), None)

        if not target:
            create_resp = self.accounts_client.create_account(
                customer_id=self.customer_id,
                account_type=account_type.value,
                initial_deposit=self.balance_checker.min_balance,
            )
            create_resp.raise_for_status()
            target = create_resp.json()

        account_id = target["id"]
        self.balance_checker.ensure_balance(account_id)
        return account_id
