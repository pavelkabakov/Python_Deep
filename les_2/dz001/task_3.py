from fractions import Fraction


def parse_fraction(frac):
    numerator, denominator = map(int, frac.split('/'))
    return numerator, denominator


def sum_and_product(frac1, frac2):
    num1, den1 = parse_fraction(frac1)
    num2, den2 = parse_fraction(frac2)

    # Сумма дробей
    sum_num = num1 * den2 + num2 * den1
    sum_den = den1 * den2
    sum_frac = f"{sum_num}/{sum_den}"

    # Произведение дробей
    product_num = num1 * num2
    product_den = den1 * den2
    product_frac = f"{product_num}/{product_den}"

    return sum_frac, product_frac


# Тестирование функции
frac1 = "1/2"
frac2 = "1/3"
sum_frac, product_frac = sum_and_product(frac1, frac2)

print(f"Сумма дробей: {sum_frac}")
print(f"Произведение дробей: {product_frac}")

# Проверка с использованием модуля fractions
print(f"Сумма дробей (fractions): {Fraction(frac1) + Fraction(frac2)}")
print(f"Произведение дробей (fractions): {Fraction(frac1) * Fraction(frac2)}")
