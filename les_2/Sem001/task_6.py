# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


balance = 5200000
count_a = 0
count_o = 0

while True:
    if balance > 5_000_000:
        print(f'налог на богатство: {balance * 0.1}')
        balance -= balance * 0.1

    action = input('Введите команду: ')
    if action == 'q':
        print(f'Ваш баланс: {balance}')
        print('Программа завершена')
        break
    elif action == 'a':
        amount = int(input('Введите сумму пополнения: '))
        if amount % 50 == 0:
            balance += amount
            count_a += 1
            if count_a % 3 == 0:
                balance *= 1.03
        else:
            print('Введена некорректная сумма!')
    elif action == 'o':
        amount = int(input('Введите сумму снятия: '))
        tax = amount * 0.015
        if tax < 30:
            tax = 30
        elif tax > 600:
            tax = 600
        if amount + tax > balance:
            print('Недостаточно средств на счете')
        else:
            if amount % 50 == 0:
                balance -= amount + tax
                count_o += 1
                if count_o % 3 == 0:
                    balance *= 1.03
            else:
                print('Введена некорректная сумма!')

    print(f'Текущий баланс: {balance}')