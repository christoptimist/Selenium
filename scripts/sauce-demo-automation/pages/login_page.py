from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

    def _enter_text(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(text)
        except TimeoutException as e:
            self.logger.error(f"Element not found: {e}")

    def _click_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException as e:
            self.logger.error(f"Element not found: {e}")

    def enter_username(self, username):
        self._enter_text(self.username_textbox, username)

    def enter_password(self, password):
        self._enter_text(self.password_textbox, password)

    def click_login(self):
        self._click_element(self.login_button)