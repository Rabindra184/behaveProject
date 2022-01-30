
@Low
Feature: Orange HRM Login

  Scenario: Login to orangehrm with valid parameter
    Given i launch chrome browser
    When i open orangehrm homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then user must successfully login to the Dashboard page
