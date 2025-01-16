from abc import ABC, abstractmethod
from selenium.webdriver.remote.webelement import WebElement

class IWebDriver(ABC):
    @abstractmethod
    def get(self,url):
        pass

    @abstractmethod
    def quit(self):
        pass

    @abstractmethod
    def find_element(self, by: str, value: str) -> WebElement:
        pass

    @abstractmethod
    def execute_script(self, string: str, value: str) -> WebElement:
        pass

    @abstractmethod
    def implicitly(self) -> WebElement:
        pass