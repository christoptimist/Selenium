from abc import ABC, abstractmethod

class IUserAgentOptions(ABC):
    @abstractmethod
    def set_user_agent(self,user_agent):
        pass