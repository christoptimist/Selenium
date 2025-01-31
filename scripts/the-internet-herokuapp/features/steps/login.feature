Feature: Website Login

  Scenario: Successful Login
    Given I am on the login page
    When I click the "Username" field and enter "correct_username"
    And I click the "Password" field and enter "correct_password"
    And I click the "Login" button
    Then I should be redirected to the home page

  Scenario: Login with Incorrect Password
    Given I am on the login page
    When I click the "Username" field and enter "correct_username"
    And I click the "Password" field and enter "incorrect_password"
    And I click the "Login" button
    Then I should see an error message "Invalid username or password"

  Scenario: Login with Empty Fields
    Given I am on the login page
    When I click the "Login" button
    Then I should see an error message "Username and password are required"