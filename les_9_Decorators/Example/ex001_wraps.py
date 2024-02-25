"""
Декоратор wraps из модуля functools в Python используется в декораторах для того, чтобы сохранить метаданные
декорируемой функции. Когда вы создаете декоратор, вы фактически заменяете одну функцию другой.
Без специальных мер это приведет к тому, что метаданные исходной функции, такие как её имя (__name__),
документация (__doc__), аннотации аргументов (__annotations__) и другие, будут потеряны, так как они заменяются
 метаданными внутренней функции декоратора.

Использование wraps помогает "обернуть" внутреннюю функцию декоратора таким образом, чтобы она казалась внешнему
 миру как исходная декорируемая функция, сохраняя при этом её метаданные.


"""

# Пример без использования wraps:
# def my_decorator(f):
#     def wrapper():
#         print("Что-то происходит перед вызовом функции.")
#         f()
#         print("Что-то происходит после вызова функции.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     """Приветствует мир."""
#     print("Привет, мир!")
#
# print(say_hello.__name__)  # Выведет 'wrapper', а не 'say_hello'
# print(say_hello.__doc__)   # Выведет None


# Пример с использованием wraps:

from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper():
        print("Что-то происходит перед вызовом функции.")
        f()
        print("Что-то происходит после вызова функции.")

    return wrapper


@my_decorator
def say_hello():
    """Приветствует мир."""
    print("Привет, мир!")


print(say_hello.__name__)  # Теперь выведет 'say_hello'
print(say_hello.__doc__)  # Теперь выведет 'Приветствует мир.'
say_hello()

"""
Использование wraps в декораторах является хорошей практикой, так как оно позволяет сохранить "идентичность"
 и метаданные декорируемой функции, что важно для отладки, автоматической генерации документации и других случаев, 
 когда метаданные функции имеют значение.
"""