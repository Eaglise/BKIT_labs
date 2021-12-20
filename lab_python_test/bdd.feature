Feature: cooking salads
  Scenario: Chief starts cooking meat salad
    Given Chief starts cooking
    When Someone ordered a meat salad
    Then The next result is expected: "Cooking meat salad..."
  Scenario: Chief starts cooking vegetarian salad
    Given Chief starts cooking
    When Someone ordered a vegetarian salad
    Then The next result is expected: "Cooking vegetarian salad..."
  Scenario: Someone asked the ingredients of a meat salad
    Given A meat salad
    When Someone asked the ingredients
    Then The next result is expected: "Salad ingredients: vegetables, meat, sauce"
  Scenario: Someone asked the ingredients of a vegetarian salad
    Given A vegetarian salad
    When Someone asked the ingredients
    Then The next result is expected: "Salad ingredients: vegetables, sauce"
  Scenario: Someone asked the ingredients of an unready salad
    Given No salad
    When Someone asked the ingredients
    Then The next result is expected: "There is no salad ready"