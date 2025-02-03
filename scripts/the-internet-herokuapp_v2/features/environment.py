from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.helpers import _load_config
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def before_all(context):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-gpu')
    context.driver = webdriver.Chrome(service=service, options=options)
    context.config = _load_config('config/configuration.yaml')
    context.driver.implicitly_wait(10)

def after_all(context):
    context.driver.quit()