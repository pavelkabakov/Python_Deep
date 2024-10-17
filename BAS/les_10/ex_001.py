# Считываем количество элементов массива
N = int(input())

# Считываем массив целых чисел
arr = list(map(int, input().split()))

# Подсчитываем количество положительных чисел
positive_count = sum(1 for x in arr if x > 0)

# Выводим результат
print(positive_count)
