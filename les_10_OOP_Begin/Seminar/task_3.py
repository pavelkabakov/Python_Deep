"""
Задание №3
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
"""


class Human:

    def __init__(self, last_name, first_name, age, sex):
        self._last_name = last_name
        self._first_name = first_name
        self._age = age
        self._sex = sex

    @property
    def age(self):
        return self._age

    @property
    def sex(self):
        return self._sex

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @age.setter
    def age(self, value):
        if value > 70:
            raise ValueError('староват')
        self.__age = value

    def up_birthday(self):
        self.__age += 1

    def get_fullname(self):
        return f'{self._last_name}, {self._first_name}'


if __name__ == "__main__":
    person = Human('Smith', 'Johan', 40, 'male')

    # print(person._first_name)
    # # print(person.__age())
    # print(person.get_age())
    # person.up_birthday()
    # print(person.get_age())
    # print(person.get_fullname())

    person.age = 40
    print(person.age)
    print(person.first_name)
    print(person.last_name)
    print(person.sex)
