from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.config_loader import load_config
import random

def before_all(context):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f'--window-size={random.randint(1200,1920)},{random.randint(800,1080)}')
    context.driver = webdriver.Chrome(service=service, options=options)
    context.config = load_config('config/dev.yaml')
    context.driver.implicitly_wait(10)

def after_all(context):
    context.driver.quit()