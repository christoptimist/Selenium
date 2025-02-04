from behave import *
from pages.web.login_page import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver, context.config)
    context.driver.get(context.config["url"]["base_url"])

@when('I click the "Username" field and enter "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)

@when('I click the "Password" field and enter "{password}"') 
def step_impl(context, password):
    context.login_page.enter_password(password)

@when('I click the "Login" button')
def step_impl(context):
    context.login_page.click_login()

@then('I should be redirected to the "{expected_results}"')
def step_impl(context, expected_results):
    assert expected_results in context.driver.current_url