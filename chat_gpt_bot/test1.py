'''
В Python, чтобы скрыть пароль, ​понадобится функция config (она находится в модуле decouple) или функции переменных окружения из модуля os. Будем работать с функцией config модуля decouple. Для установки этого модуля выполняем в терминале следующую команду:

pip install python-decouple
После установки создаем файл .env в той же папке, что и файл test.py, после чего копируем и вставляем в него идентификатор пользователя userID и пароль:

userID = 'shivi_020'
password = 'thenightwing'
Примечание: этот метод будет работать только при создании файла .env. Никакой другой формат файла не подойдет (хотя при желании можно использовать .py, .json, .ini или config.ini).

Вернемся к файлу test.py и внесем в него следующие изменения:

from decouple import config

userID = config('userID',default='')
password = config('password',default='')

print(userID, password)

'''


from decouple import config

userID = config('userID',default='')
password = config('password',default='')

print(userID, password)