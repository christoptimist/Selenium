from selenium.webdriver.common.by import By
from utilities.helpers import _enter_text_field, _click_button, _wait_element
from selenium.webdriver.remote.webelement import WebElement
import logging

class LoginPage:
    @property
    def username_id(self) -> WebElement:
        return _wait_element(self.driver, (By.ID, 'username'), self.logger)
    
    @property
    def password_id(self) -> WebElement:
        return _wait_element(self.driver, (By.ID, 'password'), self.logger)
    
    @property
    def login_button_id(self) -> WebElement:
        return _wait_element(self.driver, (By.CLASS_NAME, 'radius'), self.logger)
    
    @property
    def error_message(self) -> WebElement:
        return _wait_element(self.driver, (By.ID, 'flash'), self.logger)

    def __init__(self, driver, config):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.config = config
    
    def enter_username(self, username):
        _enter_text_field(self.driver, self.username_id, username, self.logger, self.config)

    def enter_password(self, password):
        _enter_text_field(self.driver, self.password_id, password, self.logger, self.config)

    def click_login(self):
        _click_button(self.driver, self.login_button_id, self.logger, self.config)