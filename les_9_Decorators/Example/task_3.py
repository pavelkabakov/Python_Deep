"""
Замыкания (closures) в программировании — это функции, которые запоминают своё лексическое окружение даже после того,
 как выполнились. В контексте Python, это означает, что функция, определённая внутри другой функции, может запомнить
  и иметь доступ к переменным из локального пространства имён, в котором была создана, даже после того, как внешняя
   функция завершила свою работу. Это позволяет программистам создавать некоторые из своих данных приватными, делая
    их доступными только для возвращаемой функции.

Пример замыкания в Python:
"""

def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


# Создаём замыкание
times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

# Используем замыкание
print(times3(9))  # Выведет: 27
print(times5(3))  # Выведет: 15

"""
В этом примере, make_multiplier_of является внешней функцией, а multiplier — внутренней.
 Внутренняя функция multiplier использует переменную n, которая определена в лексическом окружении внешней функции
  make_multiplier_of.
   Даже после того, как внешняя функция завершает выполнение и возвращает multiplier, multiplier сохраняет
    доступ к переменной n.
 Это и есть замыкание.

Ключевые характеристики замыканий:
Лексическое связывание: Замыкание имеет доступ к переменным внешней функции, в которой оно было определено, даже
 после того, как эта функция завершила выполнение.
Инкапсуляция: Замыкания могут использоваться для создания приватных переменных и функций, которые недоступны извне,
 за исключением через определённый интерфейс.
Сохранение состояния: Замыкания позволяют сохранять состояние между вызовами без использования глобальных переменных
 или объектов.
Замыкания широко используются в Python для реализации декораторов, функционального программирования и ситуаций, 
когда необходимо сохранить состояние без создания класса.

"""
