from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import time

# Configuration of Chrome Driver Manager
service = Service(executable_path=ChromeDriverManager().install())

# Configuration of Chrome Options
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Creation of instance of Web driver
driver = webdriver.Chrome(options=options,service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/')

language_element = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="langSelect-EN"]'))
)

language_element.click()

cookie_count_tmp = 0

while True:
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bigCookie"]'))
        )

        cookie_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cookies"]'))
        )

        cookie_button.click()
        cookie_count_tmp = int(cookie_element.text.split(' ')[0].replace(',', ''))
        print(f"Cookies: {cookie_count_tmp}")

        for index in range(4):
            try:
                product_text = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="productPrice{index}"]'))
                )

                product_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="product{index}"]'))
                )

                price_text = product_text.text.replace('"', '').replace(',', '')

                # Check if the price is not empty and then convert to int
                if price_text:
                    item_price = int(price_text)
                    if cookie_count_tmp >= item_price:
                        product_button.click()
                else:
                    print(f"Product {index} has no price or price is not available.")

            except Exception as e:
                print(f"Error processing product {index}: {e}")

    except StaleElementReferenceException as e:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cookies"]'))
        )