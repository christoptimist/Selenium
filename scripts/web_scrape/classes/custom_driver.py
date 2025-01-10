from web_scrape.interfaces.i_web_driver import IWebDriver

class CustomDriver(IWebDriver):
    def __init__(self, driver: IWebDriver):
        self._driver = driver

    def get(self, url):
        self._driver.get(url)