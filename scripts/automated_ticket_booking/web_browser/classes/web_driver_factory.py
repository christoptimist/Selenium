from seleniumwire import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from proxy.classes.residential_proxy import ResidentialProxy
from web_browser.classes.service_configuration import ServiceConfiguration
from web_browser.classes.stealth_configuration import StealthConfiguration
from web_browser.classes.chrome_options import ChromeOptions
from web_browser.interfaces.i_web_driver import IWebDriver
from web_browser.interfaces.i_web_driver_factory import IWebDriverFactory

class WebDriverFactory(IWebDriverFactory):
    def __init__(self, service_configuration: ServiceConfiguration,chrome_options: ChromeOptions, stealth_config: StealthConfiguration, residential_proxy: ResidentialProxy):
        self._service = service_configuration
        self._options = chrome_options
        self._stealth_config = stealth_config
        self._proxy = residential_proxy
        self.driver = None

    def create_driver(self) -> IWebDriver:
        # self._driver = webdriver.Chrome(service=self._service.get_service_configuration(),options=self._options.get_options(),seleniumwire_options=self._proxy.get_residential_proxy())
        self._driver = webdriver.Chrome(options=self._options.get_options())
        if self._stealth_config:
            stealth(driver=self._driver,**self._stealth_config.__dict__)
        return self._driver
        
    def quit_driver(self, driver: IWebDriver) -> None:
        if self._driver:
            driver.quit()
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")

    def find_element(self, by: str, value: str) -> WebElement:
        if self._driver:
            if by in ("xpath","id","class_name"):
                try:
                    target_element = WebDriverWait(self._driver,10).until(
                    EC.presence_of_element_located((getattr(By,by.upper(),value)))
                    )
                    return target_element
                except TimeoutException:
                    raise TimeoutException(f"Element with {by}={value} not found.")
            else:
                raise ValueError(f"Unsupported locator strategy: {by}")
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")
    
    def execute_script(self, string: str, value: str) -> WebElement:
        if self._driver:
            try:
                self._driver.execute_script(string,value)
            except TimeoutException:
                raise TimeoutException(f"javascript command: {string}={value} does not execute.")
        else:
            raise Exception("WebDriver not created yet. call create_driver() first.")
        
    def implicitly_wait(self) -> WebElement:
        if self._driver:
            return self._driver.implicitly_wait(10)
        else:
            raise Exception("WebDriver not created yet. call created_driver() first.")
        
    def custom_wait(self, timeout: int, locator: str, target_element: str) -> WebElement:
        if self._driver:
            if locator in ("xpath","id","class_name"):
                try:
                    wait_element = WebDriverWait(self._driver,timeout).until(
                        EC.presence_of_element_located((locator,target_element))
                    )
                    return wait_element
                except TimeoutException:
                    raise TimeoutException(f"Element with {locator}={target_element} not found.")
            else:
                raise ValueError(f"Unsupported locator strategy: {locator}")
        else:
            raise Exception("WebDriver not created yet. call created_driver() first.")