from abc import ABC, abstractmethod
from selenium.webdriver.remote.webelement import WebElement

class IActionChains(ABC):
    @abstractmethod
    def create_action_chains(self):
        pass