import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8000")
    GENERATE_SERVICE_URL = os.getenv("GENERATE_SERVICE_URL", "http://localhost:8001")

config = Config()
