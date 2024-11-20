# Создаем пустой список, куда будем добавлять элементы
mylist = []

# Добавляем число 5 в конец списка
mylist.append(5)

# Добавляем число 27 в конец списка
mylist.append(27)

# Добавляем число 3 в конец списка
mylist.append(3)

# Добавляем число 12 в конец списка
mylist.append(12)

# Выводим текущий список на экран (ожидается [5, 27, 3, 12])
print(mylist)

# Вставляем число 12 на позицию с индексом 1
# (сдвигая все элементы после этой позиции вправо)
mylist.insert(1, 12)

# Выводим обновленный список на экран (ожидается [5, 12, 27, 3, 12])
print(mylist)

# Выводим количество раз, которое число 12 встречается в списке
print(mylist.count(12))  # Ожидается 2, так как 12 встречается дважды

# Находим индекс первого вхождения числа 3 в списке и выводим его
print(mylist.index(3))  # Ожидается 3, так как 3 находится на индексе 3

# Выводим количество раз, которое число 5 встречается в списке
print(mylist.count(5))  # Ожидается 1, так как 5 встречается один раз

# Переворачиваем порядок элементов в списке
mylist.reverse()

# Выводим список после переворота (ожидается [12, 3, 27, 12, 5])
print(mylist)

# Сортируем элементы списка по возрастанию
mylist.sort()

# Выводим список после сортировки (ожидается [3, 5, 12, 12, 27])
print(mylist)

# Удаляем первое вхождение числа 5 из списка
mylist.remove(5)

# Выводим список после удаления (ожидается [3, 12, 12, 27])
print(mylist)

# Удаляем и сохраняем последний элемент списка
lastitem = mylist.pop()

# Выводим удалённый элемент (ожидается 27, так как это последний элемент)
print(lastitem)

# Выводим окончательное состояние списка (ожидается [3, 12, 12])
print(mylist)