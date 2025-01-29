from selenium.webdriver.common.by import By
from utilities.helpers import _enter_text, _click_element
import logging

class loginpage:
    @property
    def username_textbox(self):
        return (By.ID,"user-name")
    
    @property
    def password_textbox(self):
        return (By.ID,"password")
    
    @property
    def login_button(self):
        return (By.ID,"login-button")
    
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def enter_username(self, username):
        _enter_text(self.driver, self.username_textbox, username, self.logger)

    def enter_password(self, password):
        _enter_text(self.driver, self.password_textbox, password, self.logger)

    def click_login(self):
        _click_element(self.driver, self.login_button, self.logger)