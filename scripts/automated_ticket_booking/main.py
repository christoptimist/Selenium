from captchas.classes.recaptcha_v2_factory import ReCaptchaV2Factory
from web_browser.classes.service_configuration import ServiceConfiguration
from proxy.classes.residential_proxy import ResidentialProxy
from web_browser.classes.stealth_configuration import StealthConfiguration
from web_browser.classes.chrome_options import ChromeOptions
from web_browser.classes.web_driver_manager import WebDriverManager
from web_browser.classes.web_driver_factory import WebDriverFactory
import time

service_configurations = ServiceConfiguration()
chrome_options = ChromeOptions()
stealth_config = StealthConfiguration()
proxy = ResidentialProxy()
driver_factory = WebDriverFactory(service_configurations,chrome_options,stealth_config,proxy)
driver_manager = WebDriverManager(driver_factory)
driver = driver_manager.create_driver()

api_key = 'cdae244f9fa32337cb7dae6e087b6cfa'
target_url = 'https://google.com/recaptcha/api2/demo'
driver.get(target_url)

data_sitekey = driver.find_element("xpath",'//*[@id="recaptcha-demo"]').get_attribute('data-sitekey')

# recaptcha_factory = ReCaptchaV2Factory(api_key,target_url,data_sitekey)

print(f'Site_key: {data_sitekey}')

time.sleep(10)
driver.quit()