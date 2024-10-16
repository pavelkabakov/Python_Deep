"""
Ключевое слово nonlocal в Python используется для объявления переменных во вложенных функциях, когда необходимо
изменить значение переменной, определённой в ближайшей внешней области видимости, но не являющейся глобальной.
Это позволяет изменять переменные, находящиеся в лексическом окружении внешних функций, обеспечивая тем самым
 определённую гибкость при работе с замыканиями и вложенными функциями.

Без использования nonlocal, изменения, произведённые внутри вложенной функции, будут локальными для этой функции,
и они не повлияют на переменную с тем же именем во внешней функции. С nonlocal можно изменить значение переменной
 во внешней области видимости так, что изменения отразятся на этой переменной вне вложенной функции.

Пример использования nonlocal:
"""

def outer():
    x = "внешняя"
    def inner():
        nonlocal x  # Указываем, что хотим использовать переменную x из внешней функции
        x = "внутренняя"
        print("Внутри:", x)
    inner()
    print("Снаружи:", x)

outer()


"""
В этом примере, без nonlocal изменение переменной x в функции inner() было бы локальным для inner() и не повлияло 
бы на значение x в функции outer(). С nonlocal переменная x в inner() теперь ссылается на переменную x в outer(), 
и изменения в inner() отражаются на x в outer().

Когда использовать nonlocal:
При работе с вложенными функциями, где требуется изменить значение переменной, определённой во внешней функции.
В замыканиях, когда необходимо изменить значение захваченной переменной, не прибегая к использованию объектов или
 словарей в качестве обходного пути.
nonlocal поддерживает чистоту кода и ясность намерений при работе с вложенными функциями, предоставляя прямой способ 
модификации не-глобальных переменных во внешнем лексическом контексте.
"""