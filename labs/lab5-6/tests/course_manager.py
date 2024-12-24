class Course:
    def __init__(self, title, category):
        self.title = title
        self.category = category


class CourseManager:
    def __init__(self):
        self.courses = []

    def add_course(self, title, category):
        course = Course(title, category)
        self.courses.append(course)
        return course

    def list_courses(self):
        return [{"title": c.title, "category": c.category} for c in self.courses]