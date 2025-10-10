from core.utils import parse_response
from requests.exceptions import JSONDecodeError

class APIResponse:
    def __init__(self, response):
        self.raw = response
        self.status_code = response.status_code
        self.headers = response.headers
        self.url = response.url
        self.text = response.text
        self._data = None

    def json(self):
        try:
            data = self._data or parse_response(self.raw)
        except (ValueError, JSONDecodeError):
            text = self.raw.text.strip()
            data = {"raw": text}
        if "status" not in data:
            text = data.get("raw", "")
            data["status"] = "COMPLETED" if "Successfully" in text else "FAILED"
        return data
    
    def raise_for_status(self):
        self.raw.raise_for_status()

    def __repr__(self):
        return f"<APIResponse [{self.status_code}]>"