list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# Введите ваше решение ниже

def count_matching_numbers(list1, list2):
    # Преобразование списков в множества
    set1 = set(list1)
    set2 = set(list2)

    # Нахождение пересечения множеств
    matching_numbers = set1.intersection(set2)

    # Возвращение количества элементов в пересечении
    return len(matching_numbers)


# Вывод результата
print("Количество совпадающих чисел:", count_matching_numbers(list1, list2))