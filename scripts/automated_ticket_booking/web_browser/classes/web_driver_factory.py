from seleniumwire import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        self._driver = webdriver.Chrome(service=self._service.get_service_configuration(),options=self._options.get_options(),seleniumwire_options=self._proxy.get_residential_proxy())
        if self._stealth_config:
            stealth(driver=self._driver,**self._stealth_config.__dict__)
        return self._driver
        
    def quit_driver(self, driver: IWebDriver) -> None:
        driver.quit()

    def find_element(self, by: str, value: str) -> WebElement:
        if self._driver:
            if by.lower() == "xpath":
                target_element = WebDriverWait(self._driver,10).until(
                    EC.presence_of_element_located((By.XPATH, value))
                )
                return target_element
            elif by.lower() == "id":
                target_element = WebDriverWait(self._driver,10).until(
                    EC.presence_of_element_located((By.ID, value))
                )
                return target_element
            elif by.lower() == "class_name":
                target_element = WebDriverWait(self._driver,10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, value))
                )
                return target_element
            # Add more locator strategies as needed...
            else:
                raise ValueError(f"Unsupported locator strategy: {by}")
        else:
            raise Exception("WebDriver not created yet. Call create_driver() first.")
    
    def execute_script(self, string: str, value: str) -> WebElement:
        if self._driver:
            self._driver.execute_script(string,value)
        else:
            raise Exception("WebDriver not created yet. call create_driver() first.")
        
    def implicitly_wait(self) -> WebElement:
        if self._driver:
            return self._driver.implicitly_wait(10)
        else:
            raise Exception("WebDriver not created yet. call created_driver() first.")
