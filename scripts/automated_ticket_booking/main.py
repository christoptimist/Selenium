from web_browser.classes.user_agents import UserAgents
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
import time

user_agent = UserAgents()
service_configurations = ServiceConfiguration()
chrome_options = ChromeOptions()
chrome_options.set_user_agent(user_agent.get_random_user_agent())
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
target_url = 'https://opensea.io/'

driver.get(target_url)

time.sleep(10)
driver.quit()