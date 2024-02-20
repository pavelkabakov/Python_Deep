"""
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории

На входе:

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

На выходе:

new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

"""
import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
file_name = "test1.txt"
file_path = os.path.join(folder_path, file_name)
with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()


def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=(None, None)):
    # Путь к папке с файлами
    folder_path = 'test_folder'
    # Получаем список файлов в папке
    files = os.listdir(folder_path)
    # Фильтруем файлы по исходному расширению
    filtered_files = [file for file in files if file.endswith('.' + source_ext)]
    # Сортируем список файлов, чтобы порядок был определён
    filtered_files.sort()

    for i, filename in enumerate(filtered_files, start=1):
        # Извлекаем сохраняемую часть оригинального имени
        original_part = filename[name_range[0]:name_range[1]] if name_range[0] is not None else ''
        # Формируем новое имя файла
        new_name = f"{desired_name}{original_part}{str(i).zfill(num_digits)}.{target_ext}"
        # Полные пути к исходному и новому имени файла
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        # Переименовываем файл
        os.rename(old_file, new_file)
        # print(f"Renamed {filename} to {new_name}")


# Пример использования
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
