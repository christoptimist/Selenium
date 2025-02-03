from pages.web.common_actions import CommonActions
from selenium.webdriver.common.by import By
from utilities.decorators import retry_on_stale_element
import logging

class LoginPage(CommonActions):
    @property
    def username_id(self) -> tuple[By, str]:
        return self._wait_element(self.driver, (By.ID, 'username'), self.logging, self.config)

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.logging = logging.getLogger(__name__)

    @retry_on_stale_element(max_retries=3)
    def enter_username(self, username) -> None:
        self._enter_text_field(self.driver, self.username_id, username, self.logging, self.config)