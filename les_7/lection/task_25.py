"""
Если передать параметр size метод изменяет размер файла до указанного числа
символов или байт от начала файла.
"""

size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))