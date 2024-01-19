# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


def func_bin_or_oct_from_number(number: int, notation: int) -> str:
    res = ''
    if notation == 2 or notation == 8:
        while number > 0:
            res = str(number % notation) + res
            number = number // notation
    else:
        res += 'Расчет делается для перевода только в двоичную или восьмеричную систему исчисления'
    return res


print(func_bin_or_oct_from_number(number, notation))

print('===проверка===')
print(bin(number))
print(oct(number))