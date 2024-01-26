# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

my_list = [1, 2, 1, 4, 5, 6, 4, 9, 1, 1, 2, 4, 3]

# Решение №_1

print(*[*set(my_list)])

# Решение №_2

unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(*unique_list)