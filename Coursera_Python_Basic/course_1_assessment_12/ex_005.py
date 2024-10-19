'''
Ниже приведён список данных об ассортименте магазина, где каждый элемент списка представляет собой название товара, его количество на складе и стоимость.
Выведите каждый элемент списка в одном и том же формате, используя метод .format (а не конкатенацию строк). Например, первая строка вывода должна выглядеть
 так: The store has 12 shoes, each for 29.99 USD.
'''


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    name, stock, price = item.split(', ')
    print("The store has {}, each for {} USD.".format(stock + " " + name, price))