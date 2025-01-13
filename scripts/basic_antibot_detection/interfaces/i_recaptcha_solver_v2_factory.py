from abc import ABC, abstractmethod
from interfaces.i_recaptcha_solver_v2 import IReCaptchaV2

class IReCaptchaV2Factory(ABC):
    @abstractmethod
    def get_token(self, api_key: str, site_key: str, url: str) -> IReCaptchaV2:
        pass