"""
Если после открытия файла в коде возникнет ошибка, строка f.close() не будет
выполнена. В результате ресурсы не освободятся, возможно возникнут проблемы в
работе с открываемым файлом. Чтобы избежать подобных ошибок используют
менеджер контекста with.
"""


with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
# print(f.write('Пока'))  # ValueError: I/O operation on closed file.