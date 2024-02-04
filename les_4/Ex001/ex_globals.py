SIZE = 10

# Функция возвращает словарь переменных из глобальной области видимости, т.е. из
# пространства модуля.


def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z


print(globals())
print(func(1, 2, 3))

x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(x)