from abc import ABC, abstractmethod
from twocaptcha import TwoCaptcha

class IReCaptchaV2(ABC):
    @abstractmethod
    def get_token(self, api_key: str, site_key: str, url: str) -> TwoCaptcha:
        pass