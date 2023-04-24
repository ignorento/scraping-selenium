import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

import config
#  from decorators import social_login_required




class SocialNetworkScraper:
    def __init__(self):
        self.driver = None

    def create_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            return self.driver
        except Exception as e:
            print(e.args)