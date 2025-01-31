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
    # options.add_argument('--disable-popup-blocking')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-shm-usage')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--incognito')
    # options.add_argument('--disable-webgl')
    # options.add_argument('--disable-webrtc')
    # options.add_argument('--disable-peer-connection')
    # options.add_argument('--disable-rtc')
    # options.add_argument('--disable-rtc-surface')
    # options.add_argument('--disable-rtcdatachannel')
    # options.add_argument("--disable-cookies") 
    options.add_argument(f'--window-size={random.randint(1200,1920)},{random.randint(800,1080)}')
    context.driver = webdriver.Chrome(service=service, options=options)
    context.base_url = 'https://the-internet.herokuapp.com'
    context.config = load_config('config/login_credentials.yaml')

def after_all(context):
    context.browser.quit()