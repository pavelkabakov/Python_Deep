"""Функция внутри класса называется методом. Мы уже рассмотрели магический
метод __init__, который вызывается при создании экземпляра класса. Помимо этого
можно создавать любые методы внутри класса и обращаться к ним из экземпляра
через точечную нотацию. Различие между обращением к свойству и к методу -
круглые скобки после имени."""


class Person:


    max_up = 3


    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100


    def level_up(self):
        self.level += 1


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.level = }, {p2.level = }, {p3.level = }')
p3.level_up()
p1.level_up()
p3.level_up()
print(f'{p1.level = }, {p2.level = }, {p3.level = }')
