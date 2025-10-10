import requests
from core.settings import settings
from core.response_manager import APIResponse

class BaseHttpClient:
    def __init__(self, base_url: str = settings.BASE_URL, timeout: int = settings.TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = self.session.get(url, timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return APIResponse(response)
    
    def post(self, path: str, data=None, json=None, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = self.session.post(url, data=data, json=json, timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return APIResponse(response)
    
    


