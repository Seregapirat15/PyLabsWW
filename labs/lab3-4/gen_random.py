import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

for num in gen_random(5, 1, 3):
    print(num)  # Вывод: 5 случайных чисел от 1 до 3, например 2, 2, 3, 2, 1