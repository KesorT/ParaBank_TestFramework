from .base_http_client import BaseHttpClient
from api import endpoints

class ApiClient(BaseHttpClient):
    def get_customer_accounts(self, customer_id: int):
        path = endpoints.CUSTOMER_ACCOUNTS.format(customer_id=customer_id)
        return self.get(path)

    def get_account_details(self, account_id: int):
        path = endpoints.ACCOUNT_DETAILS.format(account_id=account_id)
        return self.get(path)
    
    def create_account(self, customer_id: int, account_type: str, initial_deposit: float):
        path = endpoints.CREATE_ACCOUNT
        params = {
            "customerId": customer_id,
            "newAccountType": account_type,
            "fromAccountId": initial_deposit
        }
        return self.post(path, params = params)

    def create_transfer(self, from_account_id: int, to_account_id: int, amount: float):
        path = endpoints.TRANSFER
        params = {
            "fromAccountId": from_account_id,
            "toAccountId": to_account_id,
            "amount": amount
        }
        return self.post(path, params = params)
    
    def pay_bill(self, from_account_id: int, to_account_id: int, amount: float, payee_name: str, payee_address: str, city: str, state: str, zip_code: str, phone: str):
        payload = {
        "payee.name": payee_name,
        "payee.address.street": payee_address,
        "payee.address.city": city,
        "payee.address.state": state,
        "payee.address.zipCode": zip_code,
        "payee.phoneNumber": phone,
        "payee.accountNumber": to_account_id,
        "amount": amount,
        "fromAccountId": from_account_id
    }
        return self.post(endpoints.BILL_PAY, json=payload)


    def login(self, username: str, password: str):
        response = self.get(endpoints.LOGIN.format(username=username, password=password))
        if response.status_code == 200:
            return response
        return {"error": "Login failed"}
    
    def deposit(self, account_id: int, amount: float):
        path = endpoints.DEPOSIT
        params = {
            "accountId": account_id,
            "amount": amount
        }
        return self.post(path, params=params)
