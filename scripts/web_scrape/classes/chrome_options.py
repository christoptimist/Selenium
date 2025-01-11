from selenium import webdriver
from interfaces.i_user_agent_options import IUserAgentOptions
from interfaces.i_window_options import IWindowOptions

class ChromeOptions(IWindowOptions, IUserAgentOptions):
    def __init__(self):
        self._options = webdriver.ChromeOptions()
        self._options.add_argument('--disable-gpu')
        self._options.add_argument('--disable-blink-features=AutomationControlled')
        self._options.add_argument('--disable-popup-blocking')
        self._options.add_argument('--no-sandbox')
        self._options.add_argument('--disable-shm-usage')
        self._options.add_argument('--incognito')

    def set_window_size(self, width, height):
        self._options.add_argument(f'--window-size={width}x{height}')

    def set_user_agent(self, user_agent):
        self._options.add_argument(f'--user-agent={user_agent}')

    def get_options(self):
        return self._options