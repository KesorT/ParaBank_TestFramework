API_PREFIX = "services/bank"

CUSTOMER_ACCOUNTS = f"{API_PREFIX}/customers/{{customer_id}}/accounts"
ACCOUNT_DETAILS = f"{API_PREFIX}/accounts/{{account_id}}"
TRANSFER = f"{API_PREFIX}/transfer"
BILL_PAY = f"{API_PREFIX}/billpay"
LOGIN = f"{API_PREFIX}/login/{{username}}/{{password}}"
DEPOSIT = f"{API_PREFIX}/deposit"
CREATE_ACCOUNT = f"{API_PREFIX}/createAccount"