from behave import *
from pages.web.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver, context.config)
    context.driver.get(context.config["url"]["base_url"])

@when('I click the Username field and enter "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)