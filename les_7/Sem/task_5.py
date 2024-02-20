"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

from random import choices, randint
from string import ascii_lowercase
from os import getcwd, makedirs, chdir

def func(ext, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files=42):
for _ in range(files):
name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
with open(name, 'wb') as data:
pass

func('.txt')

def func_2(files=10, **kwargs):
values = []
for value in kwargs.values():
values.append(value)
for _ in range(files):
ext = str(*choices(values))
func(ext, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files=5)

func_2(5, a='.txt', b='.doc', c='.exe')