"""
Задание №3
📌 Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
📌 Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой
функции.
"""

import json
import os
from typing import Callable, Any


def save_to_json(filename: str) -> Callable:
def decorator(func: Callable) -> Callable:
def wrapper(*args, **kwargs) -> Any:
result = func(*args, **kwargs)

data = {
'function_name': func.__name__,
'args': args,
'kwargs': kwargs,
'result': result
}

if os.path.exists(filename):
with open(filename, 'r') as file:
existing_data = json.load(file)

existing_data.append(data)

with open(filename, 'w') as file:
json.dump(existing_data, file, indent=2)
else:
with open(filename, 'w') as file:
json.dump([data], file, indent=2)

return result

return wrapper

return decorator


# @save_to_json("function_data.json")
def example_function(a: int, b: int, c: int = 3) -> int:
return a + b + c


# example_function(34, 56, c=555)
#
# example_function(4666, 5666, c=666)

save_to_json('function_data.json')(example_function)(10, 100, 1000)