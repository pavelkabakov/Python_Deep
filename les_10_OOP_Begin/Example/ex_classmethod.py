"""
@classmethod: Этот декоратор превращает метод класса в метод класса, что означает, что он принимает класс в качестве
 первого аргумента вместо экземпляра. Методы класса могут обращаться к атрибутам класса, но не к атрибутам
 конкретного экземпляра.
"""


class Example:
    count = 0

    def __init__(self):
        Example.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


e = Example
print(e.count)