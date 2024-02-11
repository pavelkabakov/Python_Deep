import os
from pathlib import Path

"""
Проверка на директорию, файл и ссылку
Получив информацию о содержимом текущего каталога зачастую требуется
уточнить что перед нами. В каталогах можно хранить другие каталоги и файлы. В
файлах содержатся данные. А символьные ссылки указывают на каталоги и файлы
из других мест.
Рассмотрим варианты получения информации об объектах, полученных в примере
кода выше.
"""

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')
p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')
