Feature: Duplicate courses

Scenario: Prevent adding duplicate courses
  Given I have a course titled "Python Basics" in "Programming" category
  When I add a course titled "Python Basics" in "Programming" category
  Then I should not see a duplicate course