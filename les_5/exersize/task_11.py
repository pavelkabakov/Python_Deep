# Перед вами несколько строк кода. Напишите что по вашему мнению выведет print,
# не запуская код. У вас 3 минуты.

data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)