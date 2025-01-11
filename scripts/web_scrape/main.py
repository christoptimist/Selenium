from classes.chrome_options import ChromeOptions
from classes.chrome_web_driver_factory import ChromeWebDriverFactory
from classes.stealth_configuration import StealthConfiguration
from classes.user_agents import UserAgents
from classes.web_driver_manager import WebDriverManager


user_agent = UserAgents()

chrome_options = ChromeOptions()
chrome_options.set_window_size(1200, 800)
chrome_options.set_user_agent(f'--user-agent={user_agent.get_random_user_agent()}')

stealth_config = StealthConfiguration() 

driver_factory = ChromeWebDriverFactory(chrome_options, stealth_config)
driver_manager = WebDriverManager(driver_factory)
driver = driver_manager.get_driver() 

driver.get('https://google.com/recaptcha/api2/demo')
