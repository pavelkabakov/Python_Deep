"""
Задание №2
📌 Создайте модуль с функцией внутри.
📌 Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
📌 Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
📌 Функция выводит подсказки “больше” и “меньше”.
📌 Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""

from random import randint


def guess_number(start, end, attempts):
    number = randint(start, end)
    while attempts > 0:
        my_number = int(input('Введите число: '))
        if my_number < number:
            print('Больше')
        elif my_number > number:
            print('Меньше')
        else:
            print(f'Число угадано. Число оставшихся попыток {attempts - 1}!')
        return True
        attempts -= 1
    else:
        print(f'Попытки закончились. Это было число {number}')

    return False


if __name__ == '__main__':
    print(guess_number(1, 100, 10))
