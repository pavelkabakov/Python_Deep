"""
Задание №3
📌 Улучшаем задачу 2.
📌 Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
📌 Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
📌 Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
"""

from random import randint
from sys import argv


def guess_number_com(args):
    number = randint(args[0], args[1])
    attempts = args[2]
    while attempts > 0:
        my_number = int(input('Введите число: '))
        if my_number < number:
            print('Больше')
        elif my_number > number:
            print('Меньше')
        else:
            print(f'Число угадано с {args[2] - attempts} раза!')
        return True
        attempts -= 1
    else:
        print(f'Попытки закончились. Это было число {number}')

    return False


if __name__ == '__main__':
    # print(guess_number_com(1, 100, 10))
    args = [int(elem) for elem in argv[1:]]
    print(guess_number_com(args))
