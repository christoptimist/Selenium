from behave import *
from pages.login_page import loginpage

@given('I am on the SauceDemo login page')
def step_impl(context):
    context.login_page = loginpage(context.driver)
    context.driver.get(context.config["website"]["base_url"])

@when('I enter username "standard_user" and password "secret_sauce"')
def step_impl(context):
    context.login_page.enter_username(context.config["credentials"]["username"])
    context.login_page.enter_password(context.config["credentials"]["password"])

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login()

@then('I should be redirected to the inventory page')
def step_impl(context):
    assert "inventory" in context.driver.current_url