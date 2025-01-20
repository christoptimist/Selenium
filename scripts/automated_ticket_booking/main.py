from login.classes.user_credentials import UserCredentials
from captchas.classes.recaptcha_v2_factory import ReCaptchaV2Factory
from web_interactions.classes.action_chains_factory import ActionChainsFactory
from web_interactions.classes.action_chains_manager import ActionChainsManager
from web_browser.classes.service_configuration import ServiceConfiguration
from proxy.classes.residential_proxy import ResidentialProxy
from web_browser.classes.stealth_configuration import StealthConfiguration
from web_browser.classes.chrome_options import ChromeOptions
from web_browser.classes.web_driver_manager import WebDriverManager
from web_browser.classes.web_driver_factory import WebDriverFactory
from selenium.webdriver.common.keys import Keys
import time
import random

service_configurations = ServiceConfiguration()
chrome_options = ChromeOptions()
stealth_config = StealthConfiguration()
proxy = ResidentialProxy()
driver_factory = WebDriverFactory(service_configurations,chrome_options,stealth_config,proxy)
driver_manager = WebDriverManager(driver_factory)
driver = driver_manager.create_driver()
actions_factory = ActionChainsFactory(driver)
actions_manager = ActionChainsManager(actions_factory)
actions = actions_manager.create_action_chains()

user_credentials = UserCredentials()
api_key = 'cdae244f9fa32337cb7dae6e087b6cfa'
target_url = 'https://smtickets.com/'

driver.get(target_url)

driver.implicitly_wait(10)

login_button = driver.find_element('xpath','//*[@id="headeraccount"]/button[2]')
actions.move_to_element(login_button).click().perform()

username_text_field = driver.find_element('xpath','//*[@id="username"]')
for char in user_credentials.username:
    actions.move_to_element(username_text_field).click().send_keys(char).perform()
    # imitate how the real user types
    time.sleep(random.uniform(0.00001, 0.0001)) 

password_text_field = driver.find_element('xpath','//*[@id="password"]')
for char in user_credentials.password:
    actions.move_to_element(password_text_field).click().send_keys(char).perform()
    # imitate how the real user types
    time.sleep(random.uniform(0.00001, 0.0001)) 

login_button = driver.find_element('xpath','//*[@id="loginButton"]')
actions.move_to_element(login_button).click().perform()

time.sleep(15)
driver.quit()