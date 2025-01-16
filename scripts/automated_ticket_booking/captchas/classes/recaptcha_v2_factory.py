from twocaptcha import TwoCaptcha
from captchas.interfaces.i_captcha_solver import ICaptchaSolver

class ReCaptchaV2Factory(ICaptchaSolver):
    def __init__(self, api_key, target_url, site_key):
        self.api_key = api_key
        self.target_url = target_url
        self.site_key = site_key

    def solve(self):
        solver = TwoCaptcha(self.api_key)
        bearer_token = solver.recaptcha(self.site_key,self.target_url)
        return bearer_token['code']