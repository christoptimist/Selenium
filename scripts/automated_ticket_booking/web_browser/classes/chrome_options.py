from seleniumwire import webdriver
from fake_useragent import UserAgent
import random

class ChromeOptions:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-gcpu')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--disable-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--incognito')
        self.options.add_argument(f'--window-size={random.randint(1200,1920)},{random.randint(800,1080)}')
        self.user_agent = None

    def get_user_agent(self):
        tmp = UserAgent()
        self.user_agent = tmp.random
        self.options.add_argument(f'--user-agent={self.user_agent}')
        return self.options
    
    def get_options(self):
        return self.options