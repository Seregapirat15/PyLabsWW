class Browser:
    def __init__(self, id, name, version, year):
        self.id = id
        self.name = name
        self.version = version
        self.year = year
        self.computer_id = None

class Computer:
    def __init__(self, id, model, ram):
        self.id = id
        self.model = model
        self.ram = ram
        self.browsers = []


def main():
    # Создание списков объектов классов с тестовыми данными
    browsers = [
        Browser(1, "Google Chrome", "90.0.4430.212", 2024),
        Browser(2, "Mozilla Firefox", "88.0.1", 2021),
        Browser(3, "Microsoft Edge", "90.0.818.42", 2024),
        Browser(4, "Safari", "14.0.3", 2300),
        Browser(5, "Opera", "76.0.4017.107", 2021),
        Browser(6, "Atom", "26.0.0.21", 1812),
        Browser(7, "Vivaldi", "5.5.0.0", 2023),
    ]


    computers = [
        Computer(1, "Dell Inspiron", 16),
        Computer(2, "HP Envy", 8),
        Computer(3, "Apple MacBook", 16),
        Computer(4, "Apple MacBook Pro", 32),
        Computer(5, "Apple MacBook Air", 16)
    ]


    # Связывание браузеров с компьютерами
    browsers[0].computer_id = computers[0].id
    browsers[1].computer_id = computers[0].id
    browsers[2].computer_id = computers[1].id
    browsers[3].computer_id = computers[2].id
    browsers[4].computer_id = computers[2].id
    browsers[5].computer_id = computers[3].id
    browsers[6].computer_id = computers[3].id

    computers[0].browsers = [browsers[0], browsers[1]]
    computers[1].browsers = [browsers[2]]
    computers[2].browsers = [browsers[3], browsers[4]]
    computers[3].browsers = [browsers[5], browsers[6]]

    # Вывод результатов
    print("Результаты запросов:")


    print("Запрос 1: Браузеры, у которых название начинается с буквы 'A', и названия их компьютеров.")
    result = [
        (browser.name, next((computer.model for computer in computers if computer.id == browser.computer_id), None))
        for browser in browsers
        if browser.name.startswith("A") and browser.computer_id is not None
    ]


    print(result)

    print("Запрос 2: Компьютеры с минимальной версией браузеров в каждом компьютере, отсортированные по минимальному году версии.")
    result = sorted(
    [(computer.model, min((browser.year for browser in computer.browsers), default=None)) for computer in computers],
    key=lambda x: x[1] if x[1] is not None else float('inf'),
    )


    print(result)

    print("Запрос 3: Список всех связанных браузеров и компьютеров, отсортированный по браузерам, сортировка по компьютерам произвольная.")
    result = sorted(
        [(browser.name, next((computer.model for computer in computers if computer.id == browser.computer_id), None), min(browser.year for browser in browsers if browser.computer_id == next((computer.id for computer in computers if computer.model == next((computer.model for computer in computers if computer.id == browser.computer_id), None)), None)))
         for browser in browsers
         if browser.computer_id is not None],
        key=lambda x: x[0],
    )
    print(result)


if __name__ == "__main__":
    main()