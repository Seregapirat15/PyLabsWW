class ExternalTestService:
    def run_quiz(self, quiz_data):
        print(f"Running external quiz with questions: {quiz_data}")


class LocalTestSystem:
    def start_test(self, questions):
        print(f"Starting test with questions: {questions}")


class TestAdapter:
    def __init__(self, external_service):
        self.external_service = external_service

    def start_test(self, questions):
        quiz_data = {"questions": questions}
        self.external_service.run_quiz(quiz_data)


# Использование
local_test = LocalTestSystem()
local_test.start_test(["Question 1", "Question 2"])

external_service = ExternalTestService()
adapter = TestAdapter(external_service)
adapter.start_test(["Question A", "Question B"])