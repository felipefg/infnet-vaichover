Feature: Will it rain tomorrow

# As a service user
# I want to make a request to the service
# So that i know if it will in the next 5 hours

Scenario: No rain forecast
    Given the forecast for precipitation is [0.0, 0.0, 0.0, 0.0, 0.0]
    When I make a request
    Then the response will contain "Nao vai chover"

Scenario: Heavy rain forecast
    Given the forecast for precipitation is [10.0, 10.0, 10.0, 10.0, 10.0]
    When I make a request
    Then the response will contain "Vai chover sim"

Scenario: Light rain forecast
    Given the forecast for precipitation is [2.0, 2.0, 2.0, 2.0, 2.0]
    When I make a request
    Then the response will contain "Vai chover sim"

Scenario: Light rain below threshold
    Given the forecast for precipitation is [0.0, 0.0, 0.5, 0.0, 0.0]
    And the rain threshold is 1.0
    When I make a request
    Then the response will contain "Nao vai chover"

Scenario: Light rain above threshold
    Given the forecast for precipitation is [0.0, 0.0, 0.5, 0.0, 0.0]
    And the rain threshold is 0.0
    When I make a request
    Then the response will contain "Vai chover sim"