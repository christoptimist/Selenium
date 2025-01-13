from twocaptcha import TwoCaptcha
from interfaces.i_recaptcha_solver_v2_factory import IReCaptchaV2Factory

class ReCaptchaV2Factory(IReCaptchaV2Factory):
    def __init__(self):
        pass

    def get_token(self, api_key, site_key, url):
        request = TwoCaptcha(api_key)
        token = request.recaptcha(site_key,url)
        return token['code']