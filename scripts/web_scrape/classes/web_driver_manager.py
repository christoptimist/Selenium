from web_scrape.interfaces.i_web_driver import IWebDriver
from web_scrape.interfaces.i_web_driver_factory import IWebDriverFactory

class WebDriverManager:
    def __init__(self, driver_factory: IWebDriverFactory):
        self._driver_factory = driver_factory

    def get_driver(self) -> IWebDriver:
        return self._driver_factory.create_driver()