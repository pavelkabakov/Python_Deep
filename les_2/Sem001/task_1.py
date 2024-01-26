# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

data = [1, 2, 3.142, 'string', None, True]
for item in data:
    print(type(item), end=' ')
print()
for i in range(len(data)):
    print(type(data[i]), end=' ')

