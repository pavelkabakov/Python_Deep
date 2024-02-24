"""
Чтобы добавить родительский класс Animal, мы определим в нем общие свойства и методы, которые будут наследоваться
всеми дочерними классами (Fish, Bird, и Mammal). В родительском классе можно определить общие свойства, такие
как name, и метод, например, display_info(), который затем может быть переопределен в дочерних классах для
вывода специфической информации.

В этой версии кода, класс Animal служит базовым классом для всех животных, предоставляя общее свойство name и
базовую реализацию метода display_info(). Дочерние классы (Fish, Bird, и Mammal) расширяют функционал базового
класса, добавляя специфические свойства и переопределяя метод display_info() для вывода информации, уникальной
для каждого типа животного. Использование наследования позволяет уменьшить дублирование кода и упростить структуру
программы.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Я - {self.name}, и я уникальное животное.")


class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def display_info(self):
        print(f"{self.name} живет в {'пресной' if self.water_type == 'freshwater' else 'соленой'} воде.")


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def display_info(self):
        print(f"{self.name} {'может летать' if self.can_fly else 'не может летать'}.")


class Mammal(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def display_info(self):
        print(f"{self.name} живет в {self.habitat} среде.")


# Примеры создания экземпляров каждого класса
fish = Fish("Клоун", "saltwater")
bird = Bird("Пингвин", False)
mammal = Mammal("Лев", "земля")

# Вывод информации о каждом животном
fish.display_info()
bird.display_info()
mammal.display_info()


