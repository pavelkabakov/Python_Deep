# Напишите функцию на Python, которая принимает список чисел и возвращает сумму этих чисел.
#
# Например, если на вход подается список [1, 2, 3, 4], функция должна вернуть 10.

list_numbers = [1, 2, 3, 4]

def func1(list_numbers):
    total = 0
    for i in range(len(list_numbers)):
        total += list_numbers[i]
    return total

print(func1(list_numbers))
