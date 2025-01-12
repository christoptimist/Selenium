from interfaces.i_web_driver import IWebDriver
from interfaces.i_web_driver_factory import IWebDriverFactory
from selenium.webdriver.remote.webelement import WebElement 

class WebDriverManager:
    def __init__(self, driver_factory: IWebDriverFactory):
        self._driver_factory = driver_factory

    def get_driver(self) -> IWebDriver:
        return self._driver_factory.create_driver()
    
    def quit_driver(self) -> IWebDriver:
        return self._driver_factory.quit_driver()
    
    def find_element(self, by: str, value: str) -> WebElement:
        return self._driver_factory.find_element(by, value)
    
    def execute_script(self, string: str, value: str) -> WebElement:
        return self._driver_factory.execute_script(string, value)