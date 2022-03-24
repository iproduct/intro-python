Feature: showing off behave

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  Scenario: Search for an account
    Given I search for a valid account "42"
    Then I will see the account details for "42"