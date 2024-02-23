"""
Задание №2
📌 Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
📌 После каждого ввода добавляйте новую информацию в
JSON файл.
📌 Пользователи группируются по уровню доступа.
📌 Идентификатор пользователя выступает ключём для имени.
📌 Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
📌 При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""

import json


def load_users():  # функция для загрузки данных из json - файла.
    try:
        with open('users_access.json', encoding='utf8') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return {}  # при первом запуске программы функция возвращает пустой словарь


def sort_dict(my_dict):  # Вспомогательная функция для сортировки словаря по уровню допуска
    my_dict = sorted(my_dict.items())
    my_dict = {key: value for key, value in my_dict}
    return my_dict


def access_rights():
    flag = True
    while flag:  # Бесконечный цикл
        user_name = input('Введите имя: ')
        list_id = open('text_id.txt', 'r', encoding='utf-8').read().split()  # загружаем в список сохранённые id
        print(f'Это список идентификаторов: {list_id}')  # просто проверка
        user_id = input('Введите идентификатор: ')
        if user_id in list_id:
            print('Пользователь с таким идентификатором уже зарегистрирован')
        else:
            access_level = int(input('Введите уровень доступа от 1 до 7: '))
            if 0 < access_level < 8:
                groups = load_users()  # Загружаем в функцию данные из json - файла. type(groups) -> dict
                groups[f"{access_level}"] = groups.setdefault(
                    f"{access_level}", []) + [{user_id: user_name}]
                groups = sort_dict(groups)
                with open('users_access.json', 'w', encoding='utf8') as file:  # Записываем новый словарь в json - файл
                    json.dump(groups, file, ensure_ascii=False)
                print(groups)  # Проверяем, что программа отработала корректно
                with open('text_id.txt', 'a', encoding='utf-8') as f:  # Сохраняем новый id пользователя
                    f.write(f'{user_id} ')  # !!!!!user_id СОХРАНЯЕМ С ПРОБЕЛОМ!!!!!!
            elif access_level == 0:  # Закончим корректно бесконечный цикл
                flag = False
            else:
                print('Введён некорректный код доступа')


access_rights()
