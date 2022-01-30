
@High
Feature: Orange HRM Log

   Scenario: Logo present on orangehrm homepage
    Given launch chrome browser
    When open orangehrm homepage
    Then verify that logo present on the page
    And close the browser