# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой,
# выполняя следующие операции, для выполнения которых необходимо написать следующие функции:
#
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
#
# Пополнение счета:
#
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.
#
# Снятие средств:
#
# Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть кратной
# MULTIPLICITY. При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться
# от MIN_REMOVAL до MAX_REMOVAL.
#
# Завершение работы:
#
# Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM,
# начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
#
# Проверка кратности суммы:
#
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
# Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
#
# Пример
# На входе:
#
# deposit(10000)
# withdraw(4000)
# exit()
#
# print(operations)
#
# На выходе:
#
# ['Пополнение карты на 10000 у.е. Итого 10000 у.е.',
#  'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']
#
# На входе:
# deposit(1000)
# withdraw(200)
# exit()
#
# print(operations)
#
# На выходе:
# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.',
#  'Возьмите карту на которой 770 у.е.']
#
# На входе:
# deposit(1000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()
#
# print(operations)
#
# На выходе:
# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 440 у.е.', 'Пополнение карты на 500 у.е. Итого 940 у.е.', 'Недостаточно средств. Сумма с комиссией 3045.000 у.е. На карте 940 у.е.', 'Возьмите карту на которой 940 у.е.']
#
# На входе:
# deposit(173)
# withdraw(21)
# exit()
#
# print(operations)
#
# На выходе:
# Сумма должна быть кратной 50 у.е.
# Сумма должна быть кратной 50 у.е.
# ['Недостаточно средств. Сумма с комиссией 51 у.е. На карте 0 у.е.', 'Возьмите карту на которой 0 у.е.']
#
# На входе:
# deposit(1000000000000000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()
#
# print(operations)
#
# На выходе:
# ['Пополнение карты на 1000000000000000 у.е. Итого 1000000000000000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 999999999999770 у.е.', 'Снятие с карты 300 у.е. Процент за снятие 30 у.е.. Итого 999999999999440 у.е.', 'Пополнение карты на 500 у.е. Итого 999999999999940 у.е.', 'Снятие с карты 3000 у.е. Процент за снятие 45.000 у.е.. Итого 999999999996895.000 у.е.', 'Вычтен налог на богатство 0.1% в сумме 99999999999689.5000 у.е. Итого 899999999997205.5000 у.е.', 'Возьмите карту на которой 899999999997205.5000 у.е.']

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

from decimal import Decimal, getcontext

# Установим точность вычислений для Decimal
getcontext().prec = 28

MULTIPLICITY = 50
PERCENT_REMOVAL = Decimal('0.015')  # 1.5% комиссия
MIN_REMOVAL = Decimal('30')
MAX_REMOVAL = Decimal('600')
RICHNESS_PERCENT = Decimal('0.1')  # 10% налог на богатство
RICHNESS_SUM = Decimal('10000000')  # Сумма, превышающая которую начисляется налог

bank_account = Decimal('0')
operations = []

def check_multiplicity(amount):
    return amount % MULTIPLICITY == 0

def deposit(amount):
    global bank_account
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    else:
        print("Сумма должна быть кратной 50 у.е.")

def withdraw(amount):
    global bank_account
    if check_multiplicity(amount):
        fee = max(MIN_REMOVAL, min(amount * PERCENT_REMOVAL, MAX_REMOVAL))
        total_withdraw = amount + fee
        if bank_account >= total_withdraw:
            bank_account -= total_withdraw
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {fee} у.е.. Итого {bank_account} у.е.')
        else:
            operations.append(f'Недостаточно средств. Сумма с комиссией {total_withdraw} у.е. На карте {bank_account} у.е.')
    else:
        print("Сумма должна быть кратной 50 у.е.")

def exit():
    global bank_account
    if bank_account > RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT / Decimal('100')
        bank_account -= tax
        operations.append(f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')

# deposit(1000)
# withdraw(200)
# exit()
#
# print(operations)

# # Выполнение операций с банковским счетом
# deposit(1000)
# withdraw(200)
# withdraw(300)
# deposit(500)
# withdraw(3000)
# exit()

# # Вывод списка операций
# print(operations)


deposit(1000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)