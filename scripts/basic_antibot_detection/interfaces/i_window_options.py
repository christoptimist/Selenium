from abc import ABC, abstractmethod

class IWindowOptions(ABC):
    @abstractmethod
    def set_window_size(self,width,height):
        pass
