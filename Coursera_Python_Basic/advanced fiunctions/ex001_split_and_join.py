"""
4. Напишите одну строку кода, которая выполняет следующие действия в строке " I_learn_a_lot_at_SI016":
  1. Удалите как начальные, так и конечные пробелы.
  2. Замените все "_" пробелом.
  3. Создайте список слов из полученной строки.
"""

the_string = ' I_learn_a_lot_at_SI016 '
result2 = the_string.strip().replace("_", " ").split()
print(result2)

# result = (" ".join(the_string.split("_"))).split()
# print(result)
