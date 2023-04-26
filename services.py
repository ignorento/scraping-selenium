import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

import config
from decorator import social_login_required, social_reg_required


class SocialNetworkScraper:

    BASE_URL = f"http://{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    REGISTER_URL = f"{BASE_URL}/auth/register"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = f"{BASE_URL}/user/blog"

    def __init__(self, driver=None):
        self.driver = driver or self.create_driver()
        self.is_logged_in = False
        self.is_reg_in = False


    def create_driver(self):
        """
        Create chrome driver instance
        """
        try:
            options = Options()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=options)
            return self.driver
        except Exception as e:
            print(e.args)



    def social_network_register(self):
        self.driver.get(self.REGISTER_URL)
        time.sleep(1)

        reg_username = self.driver.find_element(By.XPATH, "//form/div/input[@id='username']")
        reg_username.send_keys(config.SOCIAL_NETWORK_LOGIN)
        time.sleep(1)

        reg_email = self.driver.find_element(By.XPATH, "//form/div/input[@id='email']")
        reg_email.send_keys(config.SOCIAL_NETWORK_EMAIL)
        time.sleep(1)

        reg_password = self.driver.find_element(By.XPATH, "//form/div/input[@id='password']")
        reg_password.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        time.sleep(1)

        reg_password_confirm = self.driver.find_element(By.XPATH, "//form/div/input[@id='confirm_password']")
        reg_password_confirm.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        time.sleep(1)

        reg_first_name = self.driver.find_element(By.XPATH, "//form/div/input[@id='first_name']")
        reg_first_name.send_keys(config.SOCIAL_NETWORK_FIRST_NAME)
        time.sleep(1)

        reg_last_name = self.driver.find_element(By.XPATH, "//form/div/input[@id='last_name']")
        reg_last_name.send_keys(config.SOCIAL_NETWORK_LAST_NAME)
        time.sleep(1)

        reg_linkedin = self.driver.find_element(By.XPATH, "//form/div/input[@id='linkedin']")
        reg_linkedin.send_keys(config.SOCIAL_NETWORK_LINKEDIN)
        time.sleep(1)

        reg_facebook = self.driver.find_element(By.XPATH, "//form/div/input[@id='facebook']")
        reg_facebook.send_keys(config.SOCIAL_NETWORK_FACEBOOK)
        time.sleep(1)

        reg_facebook.send_keys(keys.Keys.ENTER)
        time.sleep(1)

        self.is_reg_in = True



    def social_network_login(self) -> object:
        # create driver & navigate to login page
        # driver = self.create_driver()
        # driver.get(self.LOGIN_URL)
        self.driver.get(self.LOGIN_URL)

        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        # username_elem1 = driver.find_element(By.ID, "username")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        password_elem.send_keys(keys.Keys.ENTER)
        self.is_logged_in = True

    @social_reg_required
    @social_login_required
    def social_network_add_post(self, title, content):

        self.driver.get(self.BLOG_URL)
        time.sleep(1)

        title_elem = self.driver.find_element(By.ID, "title")
        title_elem.send_keys(title)
        time.sleep(1)

        content_elem = self.driver.find_element(By.ID, "content")
        content_elem.send_keys(content)
        time.sleep(1)

        create_post_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        create_post_elem.click()
        time.sleep(1)

        return self.social_network_add_like()


    def social_network_add_like(self):

        like = self.driver.find_element(By.XPATH, "//div[@class='btn-group']/a[@class='btn btn-sm btn-outline-success']")
        like.click()

        return self.social_network_logout()


    def social_network_logout(self):
        logout = self.driver.find_element(By.XPATH, "//a[@href='/auth/logout']")
        logout.click()

        return self.driver
