from unittest.mock import MagicMock
from course_manager import CourseManager

class Notifier:
    def notify(self, student, course):
        print(f"Notifying {student} about new course: {course}")

def test_notification():
    notifier = Notifier()
    notifier.notify = MagicMock()

    course_manager = CourseManager()
    course_manager.add_course("Machine Learning", "AI")

    notifier.notify("Alex", "Machine Learning")
    notifier.notify.assert_called_once_with("Alex", "Machine Learning")