from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from fake_useragent import UserAgent
import random

ua_tmp = UserAgent()
user_agent = ua_tmp.random

width = random.randint(1200,1920)
height = random.randint(800,1080)

service = Service(executable_path=ChromeDriverManager().install())

# Browser configuration
option = webdriver.ChromeOptions()
option.add_argument('--disable-gpu')
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument('--disable-popup-blocking')
option.add_argument(f'--window-size={width}x{height}')
option.add_argument('--disable-extensions')
option.add_argument('--no-sandbox')
option.add_argument('--disable-shm-usage')
option.add_argument(f'--user-agent={user_agent}')
option.add_argument('--incognito')

driver = webdriver.Chrome(options=option,service=service)

stealth(
    driver=driver,
    languages=["en-US","en"],
    vendor="Google Inc",
    platform="Win32",
    webgl_vendor="Intel Inc",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True
)

driver.get('https://webscraper.io/test-sites')
driver.quit()