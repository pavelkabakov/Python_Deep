def int_to_hex(num):
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_result = ''

    if num == 0:
        return ''

    while num > 0:
        remainder = num % 16
        hex_result = hex_dict[remainder] + hex_result
        num = num // 16

    return hex_result


# Тестирование функции
num = 0
custom_hex = int_to_hex(num)
builtin_hex = hex(num)

print(f"Шестнадцатеричное представление числа: {custom_hex}")
print(f"Проверка результата: {builtin_hex}")
