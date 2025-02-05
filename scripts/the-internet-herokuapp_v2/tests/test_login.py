from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.web.login_page import LoginPage
import pytest

# @pytest.mark.parametrize(
#         "username, password, expected_results",
#         [
#             ("tomsmith","SuperSecretPassword!", True),
#             ("tomsmith","WrongPassword", False),
#             ("wrongusername","SuperSecretPassword!", False),
#             ("","", False),
#             ("user456","password456", False),
#         ]
# )
def test_login(driver, config, username, password, expected_results):
    login_page = LoginPage(driver, config, username, password, expected_results)
    driver.get(config["url"]["base_url"])
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()