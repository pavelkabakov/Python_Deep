# a = 42
# iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
list_iter = iter(data)
print(*list_iter)

# Внимание! Обратите внимание, что итератор является одноразовым
# объектом. Получив все элементы коллекции один раз он перестаёт работать.
# Для повторного извлечения элементов необходимо создать новый итератор.