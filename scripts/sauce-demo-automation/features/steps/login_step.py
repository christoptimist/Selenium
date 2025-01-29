from behave import *
from pages.login_page import loginpage

@given('I am on the SauceDemo login page')
def step_impl(context):
    context.login_page = loginpage(context.driver)
    context.driver.get("https://www.saucedemo.com/v1/")

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login()

@then('I should be redirected to the inventory page')
def step_impl(context):
    assert "inventory" in context.driver.current_url