from abc import ABC, abstractmethod
from web_scrape.interfaces.i_web_driver import IWebDriver

class IWebDriverFactory(ABC):
    @abstractmethod
    def create_driver(self) -> IWebDriver:
        pass

