Feature: Website Login

  Scenario Outline: Login with Different Credentials
    Given I am on the login page
    When I click the "Username" field and enter "<username>"
    And I click the "Password" field and enter "<password>"
    And I click the "Login" button
    Then I should be redirected to the "<expected_results>"

    Examples:
      | username      | password             | expected_results |
      | tomsmith      | SuperSecretPassword! | secure |
      | tomsmith      | WrongPassword        | login |
      | wrongusername | SuperSecretPassword! | login |
      | empty         | empty                | login |
      | user456       | password456          | login |