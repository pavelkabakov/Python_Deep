"""
пример Декоратора класса
"""

from typing import Callable


class Decorator:
    def __init__(self, num: int):
        self.num = num


    def __call__(self, func: Callable):
        def wrapper():
            return func()

        return wrapper


@Decorator(5)
def my_func():
    return 'Hello world'
