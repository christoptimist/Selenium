from selenium.webdriver.common.action_chains import ActionChains
from web_browser.classes.web_driver_manager import WebDriverManager
from web_interactions.interfaces.i_action_chains import IActionChains
from selenium.webdriver.remote.webelement import WebElement

class ActionChainsFactory(IActionChains):
    def __init__(self, driver_manager: WebDriverManager):
        self._driver_manager = driver_manager
        self.action_chains = None

    def create_action_chains(self):
        if self._driver_manager:
            self.action_chains = ActionChains(driver=self._driver_manager)
            return self.action_chains
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")    
