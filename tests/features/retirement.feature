Feature: Validating retirement month
  The calculation function needs to receive a valid integer as a month number.

  Scenario Outline: simple Month validation for retirement age program
    Given a month for a retirement age calculation
    When the month value is enteredThen the program checks if the value is a valid month between 1 and 12
    Then the program checks if the value is a valid month between 1 and 12






