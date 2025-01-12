from abc import ABC, abstractmethod
from interfaces.i_web_driver import IWebDriver
from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.support.wait import WebDriverWait

class IWebDriverFactory(ABC):
    @abstractmethod
    def create_driver(self) -> IWebDriver:
        pass

    @abstractmethod
    def quit_driver(self) -> IWebDriver:
        pass

    @abstractmethod
    def find_element(self,element) -> IWebDriver:
        pass

    @abstractmethod
    def find_element(self, by: str, value: str) -> WebElement:
        pass

    @abstractmethod
    def execute_script(self, string: str, value: str) -> WebElement:
        pass