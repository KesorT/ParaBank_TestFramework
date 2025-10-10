class AccountBalanceChecker:
    def __init__(self, accounts_client, min_balance: float = 100.0):
        self.accounts_client = accounts_client
        self.min_balance = min_balance

    def get_balance(self, account_id: int) -> float:
        resp = self.accounts_client.get_account_details(account_id)
        resp.raise_for_status()
        return float(resp.json().get("balance", 0))

    def ensure_balance(self, account_id: int):
        current_balance = self.get_balance(account_id)
        if current_balance < self.min_balance:
            required = self.min_balance - current_balance
            self.deposit(account_id, required)

    def deposit(self, account_id: int, amount: float):
        resp = self.accounts_client.deposit(account_id=account_id, amount=amount)
        resp.raise_for_status()
        return resp
