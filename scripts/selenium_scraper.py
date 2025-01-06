from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth
from fake_useragent import UserAgent
import random

# Configuration setup for service chrome.
service = Service(executable_path=ChromeDriverManager().install())

# Browser properties/Chromedriver options
option = webdriver.ChromeOptions()

# Run in headless mode (run in background)
option.add_argument('--headless')

# Disabled the AutomationControlled feature of Blink rendering engine.
option.add_argument('--disable-blink-features=AutomationControlled')

# Disabled pop-up blocking
option.add_argument('--disable-popup-blocking')

# Start the browser in maximized mode
option.add_argument('--start-maximized')

# Disable extension
option.add_argument('--disable-extensions')

# Disable sandbox mode
option.add_argument('--no-sandbox')

# Disable share memory usage
option.add_argument('--disable-dev-shm-usage')

# Create a new webdriver instance
driver = webdriver.Chrome(options=option,service=service)

# Change the property value of the navigator for webdriver to undefined
driver.execute_script("Object.defineProperty(navigator,'webdriver',{get:() => undefined})")

ua_tmp = UserAgent()
user_agent = ua_tmp.random

# Add the random pick from the list of user_agents into browser properties.
option.add_argument(f'user-agent={user_agent}')

# Apply the stealth functions to avoid detection from anti-bot.
stealth(
    driver=driver,
    languages=["en-US","en"],
    vendor="Google Inc",
    platform="Win32",
    webgl_vendor="Intel Inc",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True
)

# Test scrape
driver.get('https://opensea.io/')

html_dom = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'/html'))
)

driver.save_screenshot('screenshot.png')

driver.quit()