from behave import *
from pages.web.login_page import LoginPage
from environment import *

@given('I am on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver, context.config)
    context.driver.get(context.config["url"]["base_url"])
