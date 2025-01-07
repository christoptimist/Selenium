from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
import time
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

driver.get('https://webscraper.io/test-sites')

site_heading_element = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.XPATH,'//*[@class="site-heading"]'))
)

for product in site_heading_element:
    product_links = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,product.text))
    )

    for product_link in product_links:
        time.sleep(random.uniform(1,3))
        product_link.click()

        height = 0

        while True:
            if (height <= 30):
                height += 1
                action = ActionChains(driver)
                action.scroll_by_amount(0,height).perform()
                time.sleep(random.uniform(0.00001,0.0001))
                
    time.sleep(random.uniform(2,5))
driver.quit()