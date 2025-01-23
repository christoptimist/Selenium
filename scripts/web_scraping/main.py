from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random
import time
import csv

target_website = 'https://mb.com.ph/'

# configuration for user agent
tmp = UserAgent()
user_agent = tmp.random

# configuration for chrome properties
service = Service(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-extensions')
options.add_argument('--disable-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--incognito')
options.add_argument(f'--user-agent={user_agent}')
options.add_argument(f'--window-size={random.randint(1200,1920)},{random.randint(800,1080)}')
options.add_argument('--disable-webgl')
options.add_argument('--disable-webrtc')
options.add_argument('--disable-rtc')
options.add_argument('--disable-rtc-surface')
options.add_argument('--disable-rtcdatachannel')
options.add_argument('--disable-cookies')
options.add_argument('--disable-images')
options.add_argument('--autoplay-policy=no-user-gesture-required')

# configuration for proxy
proxy_options = {
        'proxy': {
        'http': "http://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2334",
        'https': "https://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2334",
        'http': "socks5://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2333",
        'https': "socks5://u2e1195a156ca05c4-zone-custom:u2e1195a156ca05c4@43.152.113.55:2333"
    }
}

# Applying the properties of chrome.
"""
    The first instance of driver is using the proxy server.
    Purpose: To hide the real ip address and avoiding getting block by the target website.
    Instructions: Kindly uncomment the code line 39 up to 46.
"""
#driver = webdriver.Chrome(service=service,options=options,seleniumwire_options=proxy_options)

"""
    Without using rotating proxy.
"""
driver = webdriver.Chrome(service=service,options=options)

# Applying the basic antibot detection
stealth(driver,
    languages = ["en-US","en"], 
    vendor = "Google Inc.",
    platform = "Win32",
    webgl_vendor = "Intel Inc.",
    renderer = "Intel Iris OpenGL Engine",
    fix_hairline = True
)

# Accessing the target website.
driver.get(target_website)

main_container = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/main/div/div/div/div[1]/div[2]'))
)

html_source = main_container.get_attribute('innerHTML')

soup = BeautifulSoup(html_source,'lxml')
main_group = soup.find('div',class_="row justify-center")
groups = main_group.find_all('div',class_="article-list mx-auto d-flex flex-column")

with open('news_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['tags','news','hyperlink']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for group in groups:
        article_tags = group.find('h1',class_="mb-font-live-update-subhead mb-2").text.strip()
        news_articles = group.find_all('div',class_="row")
        for news in news_articles:
            article_title = news.find('span',"mb-font-live-update-article-title lu-two-rows text-left").text.strip()
            article_hyperlink = news.find('a',class_="custom-text-link").get('href')
            writer.writerow({
                'tags': article_tags,
                'news': article_title,
                'hyperlink': article_hyperlink
            })

time.sleep(10)
driver.quit()
