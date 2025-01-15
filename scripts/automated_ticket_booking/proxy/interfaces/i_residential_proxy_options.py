from abc import ABC, abstractmethod

class IResidentialProxyOptions(ABC):
    @abstractmethod
    def get_residential_proxy(self):
        pass