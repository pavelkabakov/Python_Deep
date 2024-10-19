'''
Заполнить двумерный массив размером 5*5 случайными числами в диапазоне от 10
до 100. Найти в массиве количество повторений каждого числа.
'''

import random

random_array = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
print('Исходный массив')
for row in random_array:
    for element in row:
        print(element, end=" ")
    print()

for i, row in enumerate(random_array):
    for j, element in enumerate(row):
        random_array[i][j] = random.randint(10, 100)
print('Массив заполненный случайным числами от 10 до 100')
for row in random_array:
    for element in row:
        print(element, end=" ")

print()
