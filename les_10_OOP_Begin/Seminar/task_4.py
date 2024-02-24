"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""

from random import randint

from task_3 import Human


class Employee(Human):
    def __init__(self, first_name, last_name, age, sex, employee_id):
        super().__init__(first_name, last_name, age, sex)
        self.employee_id = employee_id
        self.access_level = self.employee_id % 7


andrey = Employee('Andrey', 'Egorov', 23, 'men', 567989)

print(andrey.employee_id)
print(andrey.first_name)
print(andrey.last_name)
print(andrey.age)
print(andrey.sex)
print(andrey.access_level)

"""
class Employee(Human):

    def get_id(self):
        self._id = randint(100000, 999999)
        return self._id

    def get_level(self):
        self._level = sum(int(i) for i in str(self._id)) % 7
        return self._level


employee = Employee('Петров', 'Саня', 45)

print(employee._last_name)
print(employee.get_age())

print(employee.get_fullname())
print(employee.get_id())
print(employee.get_level())
"""
