from selenium.webdriver.common.action_chains import ActionChains
from web_browser.classes.web_driver_manager import WebDriverManager
from web_interactions.interfaces.i_action_chains import IActionChains

class ActionChainsFactory(IActionChains):
    def __init__(self, driver_manager: WebDriverManager):
        self._driver_manager = driver_manager
        self.action_chains = None

    def create_action_chains(self):
        if self._driver_manager:
            self.action_chains = ActionChains(self._driver_manager)
            return self.action_chains
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")    
    
    def move_to_element(self, target_element):
        if self._driver_manager:
            destination = self.action_chains.move_to_element(target_element)
            return destination
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")