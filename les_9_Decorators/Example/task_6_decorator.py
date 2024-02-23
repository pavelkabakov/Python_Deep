"""
Декораторы с аргументами:
Иногда необходимо, чтобы декораторы могли принимать аргументы, как и обычные функции. Это можно реализовать,
 добавив ещё один уровень вложенных функций:
"""


def repeat(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(times=3)
def say_hello(name):
    print(f"Привет, {name}!")


say_hello("Мир")

"""
В этом примере repeat — это декоратор, который принимает аргумент times и позволяет вызвать декорируемую функцию
 times раз.

Декораторы в стандартной библиотеке Python:
Python включает несколько декораторов в стандартную библиотеку, в том числе @staticmethod и @classmethod для 
методов класса, а также @property для создания свойств класса.

Практическое применение:
Декораторы широко используются в веб-разработке, например, во Flask и Django для маршрутизации URL-адресов и 
контроля доступа. Они также используются в множестве других областей, где требуется динамически модифицировать 
или расширять поведение функций.

Декораторы делают код более чистым, читаемым и поддерживаемым, позволяя изолировать функциональность модификации
поведения от самой бизнес-логики.
"""
