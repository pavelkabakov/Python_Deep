"""
В Python для получения доступа файлу используют функцию open().
open(file, mode='r', buffering=-1, encoding=None, errors=None,
newline=None, closefd=True, opener=None)
"""

f = open('text_data.txt', encoding='utf-8')
print(f)
print(list(f))