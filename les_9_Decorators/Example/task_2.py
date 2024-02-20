"""
Декораторы в Python — это мощный инструмент, позволяющий модифицировать поведение функций или методов без изменения их
 кода. Они предоставляют простой способ применения одинаковой логики к нескольким функциям или методам, облегчая
 тем самым управление кодом и его поддержку. Вот основные причины использования декораторов:

Улучшение читаемости и поддерживаемости кода: Декораторы помогают избавиться от повторяющегося кода, сосредотачивая
общую функциональность в одном месте. Это делает код проще для понимания и поддержки.

Добавление функциональности: С помощью декораторов можно легко добавлять дополнительную функциональность к существующим
функциям или методам, не изменяя их код. Это особенно полезно, когда вы работаете с кодом, который вы не можете или
 не хотите изменять напрямую.

Применение аспектно-ориентированного программирования: Декораторы позволяют реализовывать аспектно-ориентированные
решения, где вы можете инъецировать код для выполнения задач логирования, кеширования, контроля доступа и т.д.,
не затрагивая бизнес-логику.

Логирование и отладка: Декораторы могут автоматически логировать вызовы функций и их результаты, что упрощает отладку
и мониторинг приложений.

Проверка предусловий и постусловий: Можно использовать декораторы для проверки входных и выходных данных функций,
 обеспечивая таким образом соблюдение контрактов функций.

Кеширование результатов: Декораторы могут использоваться для кеширования результатов выполнения функций, что полезно
для оптимизации производительности, особенно если функции выполняют ресурсоемкие вычисления.

Авторизация и аутентификация: В веб-разработке декораторы часто применяются для контроля доступа к определенным
ресурсам, проверяя, имеет ли пользователь необходимые права доступа.

Пример использования декоратора

В этом примере декоратор my_decorator добавляет дополнительные действия до и после вызова функции say_hello, не изменяя
 её первоначальную реализацию.

Декораторы делают код более гибким и читаемым, позволяя легко расширять и модифицировать поведение функций.
"""

def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед вызовом функции.")
        func()
        print("Что-то происходит после вызова функции.")

    return wrapper

@my_decorator
def say_hello():
    print("Привет, мир!")


say_hello()