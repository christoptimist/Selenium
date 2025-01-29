import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import loginpage
import random
import logging

class testsaucedemologin(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--incognito')
        options.add_argument('--disable-webgl')
        options.add_argument('--disable-webrtc')
        options.add_argument('--disable-peer-connection')
        options.add_argument('--disable-rtc')
        options.add_argument('--disable-rtc-surface')
        options.add_argument('--disable-rtcdatachannel')
        options.add_argument("--disable-cookies") 
        options.add_argument(f'--window-size={random.randint(1200,1920)},{random.randint(800,1080)}')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.loginpage = loginpage(self.driver)
        self.driver.implicitly_wait(10)
        self.logger = logging.getLogger(__name__)

    def test_successful_login(self):
        self.driver.get("https://www.saucedemo.com/v1/")
        self.loginpage.enter_username("standard_user")
        self.loginpage.enter_password("secret_sauce")
        self.loginpage.click_login()
        self.assertIn("inventory", self.driver.current_url)
        self.logger.info("Login successful")

    def tearDown(self):
        self.logger.info("Test completed")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()