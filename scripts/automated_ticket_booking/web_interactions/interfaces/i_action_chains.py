from abc import ABC, abstractmethod
from selenium.webdriver.remote.webelement import WebElement

class IActionChains(ABC):
    @abstractmethod
    def create_action_chains(self):
        pass

    @abstractmethod
    def move_to_element(self,target_element) -> WebElement:
        pass
    