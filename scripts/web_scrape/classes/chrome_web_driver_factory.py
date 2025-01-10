from selenium import webdriver
from selenium_stealth import stealth
from web_scrape.classes.chrome_options import ChromeOptions
from web_scrape.classes.stealth_configuration import StealthConfiguration
from web_scrape.interfaces.i_web_driver import IWebDriver
from web_scrape.interfaces.i_web_driver_factory import IWebDriverFactory

class ChromeWebDriverFactory(IWebDriverFactory):
    def __init__(self,options: ChromeOptions, stealth_config: StealthConfiguration):
        self._options = options
        self._stealth_config = stealth_config

    def create_driver(self) -> IWebDriver:
        driver = webdriver.Chrome(options=self._options.get_options())
        if self._stealth_config:
            stealth(driver=driver,**self._stealth_config.__dict__)
        return driver
        
        