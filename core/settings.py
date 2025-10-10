import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://parabank.parasoft.com/parabank/")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    TIMEOUT = int(os.getenv("TIMEOUT", 20))
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    
        
settings = Settings()

