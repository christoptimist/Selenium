Feature: Website Login

  Scenario Outline: Login with Different Credentials
    Given I am on the login page
    When I click the "Username" field and enter "<username>"

    Examples:
      | username      |
      | tomsmith      |
      | tomsmith      |
      | wrongusername |
      | empty         |
      | user456       |