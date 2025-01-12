from interfaces.i_recaptcha_solver_v2 import IReCaptchaV2
from interfaces.i_recaptcha_solver_v2_factory import IReCaptchaV2Factory

class ReCaptchaManager:
    def __init__(self, recaptcha_factory : IReCaptchaV2Factory):
        self._recaptcha_factory = recaptcha_factory

    def get_token(self, api_key: str, site_key: str, url: str) -> IReCaptchaV2:
        return self._recaptcha_factory.get_token(api_key, site_key, url)