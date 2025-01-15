from classes.service_configuration import ServiceConfiguration
from proxy.classes.residential_proxy import ResidentialProxy
from classes.stealth_configuration import StealthConfiguration
from classes.chrome_options import ChromeOptions
from classes.web_driver_manager import WebDriverManager
from classes.web_driver_factory import WebDriverFactory
import time

service_configurations = ServiceConfiguration()
chrome_options = ChromeOptions()
stealth_config = StealthConfiguration()
proxy = ResidentialProxy()
driver_factory = WebDriverFactory(service_configurations,chrome_options,stealth_config,proxy)
driver = WebDriverManager(driver_factory)

driver = driver.create_driver()

driver.get('https://www.showmyip.com/')

time.sleep(15)
driver.quit()