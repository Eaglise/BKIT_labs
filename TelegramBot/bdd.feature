Feature: Functions checking
  Scenario: Checking an existing city
    Given An existing city
    When Trying to check it
    Then The next result is expected: "False"
  Scenario: Checking a non-existing city
    Given A non-existing city
    When Trying to check it
    Then The next result is expected: "True"
  Scenario: Sending a normal image request
    Given A normal image request
    When Finding image
    Then We expect to receive an image
  Scenario: Sending a weird image request
    Given A weird image request
    When Finding image
    Then The next result is expected: "ERROR"