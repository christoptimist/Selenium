from pages.web.common_actions import CommonActions
from selenium.webdriver.common.by import By
import logging

class LoginPage(CommonActions):
    @property
    def username_id(self) -> tuple[By, str]:
        return self._wait_element(self.driver, (By.ID, 'username'), self.logging, self.config)
    
    @property
    def password_id(self) -> tuple[By, str]:
        return self._wait_element(self.driver, (By.ID, 'password'), self.logging, self.config)
    
    @property
    def button_id(self) -> tuple[By, str]:
        return self._wait_element(self.driver, (By.CLASS_NAME, 'radius'), self.logging, self.config)

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.logging = logging.getLogger(__name__)

    def enter_username(self, username) -> None:
        self._enter_text_field(self.driver, self.username_id, username, self.logging, self.config)

    def enter_password(self, password) -> None:
        self._enter_text_field(self.driver, self.password_id, password, self.logging, self.config)

    def click_login(self) -> None:
        self._click_button(self.driver, self.button_id, self.logging, self.config)