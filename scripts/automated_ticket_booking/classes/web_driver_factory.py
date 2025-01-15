from seleniumwire import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from proxy.classes.residential_proxy import ResidentialProxy
from classes.service_configuration import ServiceConfiguration
from classes.stealth_configuration import StealthConfiguration
from classes.chrome_options import ChromeOptions
from interfaces.i_web_driver import IWebDriver
from interfaces.i_web_driver_factory import IWebDriverFactory

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