import pytest
from course_manager import CourseManager

@pytest.fixture
def course_manager():
    """Фикстура для инициализации CourseManager с тестовыми данными."""
    manager = CourseManager()
    manager.add_course("Python Basics", "Programming")
    manager.add_course("Data Science", "Data Analysis")
    return manager

def test_add_course(course_manager):
    """Тест добавления нового курса."""
    new_course = course_manager.add_course("Machine Learning", "AI")
    assert new_course.title == "Machine Learning"
    assert new_course.category == "AI"
    assert len(course_manager.list_courses()) == 3

def test_list_courses(course_manager):
    """Тест получения списка курсов."""
    courses = course_manager.list_courses()
    assert len(courses) == 2
    assert courses[0]["title"] == "Python Basics"
    assert courses[1]["category"] == "Data Analysis"

def test_no_duplicate_courses(course_manager):
    """Тест, чтобы убедиться, что дублирующиеся курсы не добавляются."""
    course_manager.add_course("Python Basics", "Programming")
    courses = course_manager.list_courses()
    assert len(courses) == 2  # Список остается неизменным

def test_empty_course_list():
    """Тест, что при пустом менеджере список курсов пуст."""
    manager = CourseManager()
    courses = manager.list_courses()
    assert courses == []