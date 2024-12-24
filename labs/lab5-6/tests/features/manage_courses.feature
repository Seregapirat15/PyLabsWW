Feature: Course management

  Scenario: Add a course to the system
    Given I have an empty course list
    When I add a course titled "Python Basics" in "Programming" category
    Then I should see the course in the list