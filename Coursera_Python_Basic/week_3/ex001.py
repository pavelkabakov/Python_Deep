'''
rainfall_mi Это строка, содержащая среднее количество осадков в Мичигане за каждый месяц (в дюймах), где каждый месяц разделён запятой. Напишите код для вычисления количества месяцев, в которых выпадает более 3 дюймов осадков. Сохраните результат в переменной num_rainy_months. Другими словами, посчитайте количество элементов со значениями > 3.0.

Жестко заданные ответы не будут засчитаны.
'''

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
list = rainfall_mi.split(", ")
num_rainy_months = 0
print(list)

for i in list:
    if float(i) > 3.0:
        num_rainy_months += 1

print(num_rainy_months)