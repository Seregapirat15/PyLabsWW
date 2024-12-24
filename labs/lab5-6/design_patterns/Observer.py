class CourseNotifier:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, course):
        for observer in self._observers:
            observer.update(course)


class Student:
    def __init__(self, name):
        self.name = name

    def update(self, course):
        print(f"{self.name}, новый курс доступен: {course}")


# Использование
notifier = CourseNotifier()

student1 = Student("Алексей")
student2 = Student("Мария")

notifier.subscribe(student1)
notifier.subscribe(student2)

notifier.notify("Python для начинающих")  
# Алексей, новый курс доступен: Python для начинающих
# Мария, новый курс доступен: Python для начинающих