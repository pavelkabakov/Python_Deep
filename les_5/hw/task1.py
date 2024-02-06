"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

Пример использования.
На входе:

file_path = "C:/Users/User/Documents/example.txt"

На выходе:

('C:/Users/User/Documents/', 'example', '.txt')

на входе:
file_path = 'file_in_current_directory.txt'

на выходе:
('', 'file_in_current_directory', '.txt')
"""

import os


def get_file_info(file_path):
    # Разделяем путь на путь к каталогу и имя файла
    dir_path, filename = os.path.split(file_path)

    # Добавляем слеш к пути каталога, если он не пустой и не заканчивается на слеш
    if dir_path and not dir_path.endswith(os.path.sep):
        dir_path += os.path.sep

    # Разделяем имя файла на имя без расширения и расширение
    file_name, file_extension = os.path.splitext(filename)

    # Возвращаем кортеж с путем к каталогу, именем файла и расширением
    return (dir_path, file_name, file_extension)


# Пример использования
file_path1 = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path1))

file_path2 = 'file_in_current_directory.txt'
print(get_file_info(file_path2))
