Feature: Adding extras to drinks

  Scenario: Add whipped cream to cappuccino

    Given i have cappuccino
    When i add whipped cream
    Then my drink must have the name "Cappuccino, with whipped cream"
    And my drink must have the price 2.30