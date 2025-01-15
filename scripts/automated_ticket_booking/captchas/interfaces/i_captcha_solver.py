from abc import ABC, abstractmethod

class ICaptchaSolver(ABC):
    @abstractmethod
    def solve(self):
        pass