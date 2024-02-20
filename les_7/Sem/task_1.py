"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

import random


def rnd_nums():
    return f'{str(random.randint(-1000, 1000))} | {str(round(random.uniform(-1000, 1000), 3))}\n'


def write_nums(name_file, count):
    for _ in range(count):
        with open(name_file, 'a', encoding='utf-8') as f:
            f.write(rnd_nums())


write_nums('text_nums.txt', 5)
