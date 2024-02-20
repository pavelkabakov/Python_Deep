"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
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

def func_3(dir):
my_path = getcwd() + dir
try:
makedirs(my_path)
chdir(my_path)
except FileExistsError:
chdir(my_path)
func_2(5, a='.txt', b='.doc', c='.exe')
chdir('..')

func_3('test_dir')