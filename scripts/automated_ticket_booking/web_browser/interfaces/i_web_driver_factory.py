from abc import ABC, abstractmethod
from web_browser.interfaces.i_web_driver import IWebDriver
from selenium.webdriver.remote.webelement import WebElement

class IWebDriverFactory(ABC):
    @abstractmethod
    def create_driver(self) -> IWebDriver:
        pass

    @abstractmethod
    def quit_driver(self) -> IWebDriver:
        pass

    @abstractmethod
    def find_element(self) -> WebElement:
        pass

    @abstractmethod
    def execute_script(self) -> WebElement:
        pass

    @abstractmethod
    def webdriverwait(self) -> WebElement:
        pass