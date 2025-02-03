from pages.web.common_actions import CommonActions
from selenium.webdriver.common.by import By
import logging

class LoginPage(CommonActions):
    @property
    def username_id(self) -> tuple[By, str]:
        return self._wait_element(self.driver, (By.ID, 'username'), self.logging, self.config)
    
    def __init__(self, driver, config):
        self.driver = driver,
        self.config = config,
        self.logging = logging.getLogger(__name__)