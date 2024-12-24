from behave import given, when, then
from course_manager import CourseManager

@given("I have an empty course list")
def step_given_empty_course_list(context):
    context.manager = CourseManager()

@when('I add a course titled "{title}" in "{category}" category')
def step_when_add_course(context, title, category):
    context.manager.add_course(title, category)

@then("I should see the course in the list")
def step_then_see_course_in_list(context):
    courses = context.manager.list_courses()
    assert len(courses) == 1
    assert courses[0]["title"] == "Python Basics"
    assert courses[0]["category"] == "Programming"