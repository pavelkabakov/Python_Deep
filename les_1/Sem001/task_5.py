
# 📌 Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# 📌 Используйте while и if.
# 📌 Попробуйте разные значения e и n.

n, e = 10 , 3
new_sum = 0
elem = 0
while elem <= n:
    elem += 1
    if elem %2 == 0:
        if elem % e == 0:
            continue
        new_sum += elem
print(f'Сумма частных элементов от 1 до n исключая кратные e - {new_sum}')