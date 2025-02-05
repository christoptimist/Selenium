from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities.helpers import _load_config
from pages.web.login_page import LoginPage
import pytest

@pytest.mark.parametrize(
        "username, password, expected_results",
        [
            ("tomsmith","SuperSecretPassword!", True),
            ("tomsmith","WrongPassword", False),
            ("wrongusername","SuperSecretPassword!", False),
            ("","", False),
            ("user456","password456", False),
        ]
)
def test_login(driver):
    login_page = LoginPage(driver)
    driver.get('https://the-internet.herokuapp.com/login')