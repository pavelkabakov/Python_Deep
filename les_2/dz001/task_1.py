def to_hex_string(num):
    # Преобразование числа в шестнадцатеричное представление
    hex_representation = "%X" % num
    return hex_representation

# Тестирование функции
num = 0
hex_string = to_hex_string(num)
print("Шестнадцатеричное представление числа:", hex_string)
print("Проверка результата:", hex(num))
