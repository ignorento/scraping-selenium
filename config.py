import os
from dotenv import load_dotenv

load_dotenv()

SOCIAL_NETWORK_LOGIN = os.getenv("SOCIAL_NETWORK_LOGIN")
SOCIAL_NETWORK_PASSWORD = os.getenv("SOCIAL_NETWORK_PASSWORD")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
