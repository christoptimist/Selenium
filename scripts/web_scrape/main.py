from classes.chrome_options import ChromeOptions
from classes.chrome_web_driver_factory import ChromeWebDriverFactory
from classes.stealth_configuration import StealthConfiguration
from classes.user_agents import UserAgents
from classes.web_driver_manager import WebDriverManager
from classes.recaptcha_v2_factory import ReCaptchaV2Factory
from classes.recaptcha_v2_manager import ReCaptchaManager
import time

user_agent = UserAgents()

chrome_options = ChromeOptions()
chrome_options.set_window_size(1200, 800)
chrome_options.set_user_agent(f'--user-agent={user_agent.get_random_user_agent()}')

stealth_config = StealthConfiguration() 

driver_factory = ChromeWebDriverFactory(chrome_options, stealth_config)
driver_manager = WebDriverManager(driver_factory)
driver = driver_manager.get_driver() 

captcha_factory = ReCaptchaV2Factory()
captcha_manager = ReCaptchaManager(captcha_factory)
website = 'https://google.com/recaptcha/api2/demo'
driver.get(website)

site_key = driver.find_element('xpath', '//*[@id="recaptcha-demo"]').get_attribute('data-sitekey')
textarea_element = driver.find_element('xpath', '//*[@id="g-recaptcha-response"]')
token = captcha_manager.get_token('api_key', site_key,website)
driver.execute_script("arguments[0].style.display = 'block';", textarea_element)
textarea_element.send_keys(token)
button_element = driver.find_element('xpath', '//*[@id="recaptcha-demo-submit"]')
button_element.click()

driver.quit()
