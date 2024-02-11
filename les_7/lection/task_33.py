import os
from pathlib import Path

"""
В операционной системе Windows для указания пути используется обратный слеш \.
В Unix системах путь разделяется слешем. Чтобы программа работала одинаково на
любой ОС рекомендуется использовать специальную функцию join из os.path для
склеивания путей.
Модуль pathlib использует более понятный приём с переопределением операции
деления.
"""

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')
file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')
