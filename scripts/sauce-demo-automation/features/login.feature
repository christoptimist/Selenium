Feature: Login to SauceDemo
  As a user
  I want to login to SauceDemo
  So that I can access the inventory page

  Scenario: Successful login with valid credentials
    Given I am on the SauceDemo login page
    When I enter username "standard_user" and password "secret_sauce"
    And I click the login button
    Then I should be redirected to the inventory page