from pages.web.common_actions import CommonActions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import logging

class LoginPage(CommonActions):
    @property
    def username_id(self) -> WebElement:
        return self._wait_element(self.driver, (By.ID, 'username'), self.logging)
    
    def __init__(self, driver, config):
        self.driver = driver,
        self.config = config,
        self.logging = logging.getLogger(__name__)

    def enter_username(self, username):
        self._enter_text_field(self.driver, self.username_id, username, self.logging)