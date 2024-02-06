"""
Создайте функцию генератор чисел Фибоначчи fibonacci.
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

Пример использования.
На входе:

f = fibonacci()
for i in range(10):
    print(next(f))

На выходе:

0
1
1
2
3
5
8
13
21
34

Этот код определяет функцию fibonacci, которая инициализирует две переменные a и b значениями 0 и 1 соответственно.
 В бесконечном цикле while True функция сначала возвращает текущее значение a с помощью оператора yield,
 а затем обновляет значения a и b так, чтобы они соответствовали следующей паре чисел Фибоначчи.

Каждый вызов next(f) в цикле for инициирует выполнение функции fibonacci до следующего оператора yield,
что позволяет получить следующее число Фибоначчи в последовательности.

"""

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования
f = fibonacci()
for i in range(10):
    print(next(f))


