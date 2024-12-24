import json
import sys
import random
import os
import time

def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned:")
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result
    return wrapper

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"time: {elapsed_time:.1f}")

from contextlib import contextmanager


path = os.path.join(os.path.dirname(__file__), "data_light.json")

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(set(item['job-name'].lower() for item in arg))

@print_result
def f2(arg):
    return list(filter(lambda item: item.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda item: item + ' с опытом Python', arg))

@print_result
def f4(arg):
    salaries = [random.randint(100000, 200000) for _ in arg]
    return list(zip(arg, salaries))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))