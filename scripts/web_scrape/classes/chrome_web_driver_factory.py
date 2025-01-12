from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
from classes.chrome_options import ChromeOptions
from classes.stealth_configuration import StealthConfiguration
from interfaces.i_web_driver import IWebDriver
from interfaces.i_web_driver_factory import IWebDriverFactory
from selenium.webdriver.remote.webelement import WebElement

class ChromeWebDriverFactory(IWebDriverFactory):
    def __init__(self,options: ChromeOptions, stealth_config: StealthConfiguration):
        self._options = options
        self._stealth_config = stealth_config
        self._driver = None

    def create_driver(self) -> IWebDriver:
        driver = webdriver.Chrome(options=self._options.get_options())
        self._driver = driver
        if self._stealth_config:
            stealth(driver=self._driver,**self._stealth_config.__dict__)
        return self._driver
    
    def quit_driver(self) -> None:
        if self._driver:
            self._driver.quit()
            self._driver = None
    
    def find_element(self, by: str, value: str) -> WebElement:
        if self._driver:
            if by == "xpath":
                return self._driver.find_element(By.XPATH, value)
            elif by == "id":
                return self._driver.find_element(By.ID, value)
            elif by == "class_name":
                return self._driver.find_element(By.CLASS_NAME, value)
            # Add more locator strategies as needed 
            else:
                raise ValueError(f"Unsupported locator strategy: {by}")
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")
        
    def execute_script(self, string, value):
        if self._driver:
            return self._driver.execute_script(string, value)
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")
