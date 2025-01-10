from abc import ABC, abstractmethod

class IWebDriver(ABC):
    @abstractmethod
    def get(self,url):
        pass