from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_name(self):
        print('abstract metod')

    def get_surname(self):
        print('not abstract')


class Bird(Animal):
    def get_name(self):
        print('abstract metod')


b = Bird()
b.get_name()