"""
Декораторы в Python — это мощный и выразительный инструмент для модификации поведения функций или методов, не изменяя
 их кода напрямую. Декораторы позволяют "оборачивать" одну функцию вокруг другой, тем самым расширяя или изменяя её
 поведение. Это достигается за счет использования функций высшего порядка, то есть функций, которые могут принимать
 другие функции в качестве аргументов и/или возвращать их. Декораторы часто используются для логирования, измерения
 времени выполнения, обеспечения контроля доступа, кеширования и многих других задач.

Базовый пример декоратора:
"""


def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед вызовом функции.")
        func()
        print("Что-то происходит после вызова функции.")

    return wrapper


@my_decorator
def say_hello():
    print("Привет, мир!")


say_hello()

"""
В этом примере my_decorator — это декоратор, который оборачивает функцию say_hello. Когда вы вызываете say_hello(),
 Python сначала вызывает my_decorator(say_hello), который возвращает функцию wrapper. Эта функция wrapper выполняет
  код до и после вызова say_hello, тем самым модифицируя её поведение без изменения самой функции say_hello.
"""