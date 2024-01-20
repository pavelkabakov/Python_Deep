a = 5
b = 5
c = 10


# Введите ваше решение ниже

def check_triangle(a, b, c):
    # Проверка существования треугольника
    if a >= b + c or b >= a + c or c >= a + b:
        return "Треугольник не существует"

    # Определение типа треугольника
    if a == b == c:
        return "Треугольник существует\nТреугольник равносторонний"
    elif a == b or b == c or a == c:
        return "Треугольник существует\nТреугольник равнобедренный"
    else:
        return "Треугольник существует\nТреугольник разносторонний"


print(check_triangle(a, b, c))