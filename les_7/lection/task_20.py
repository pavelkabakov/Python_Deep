"""
● print в файл
Функция print по умолчанию выводит информацию в поток вывода. Обычно это
консоль. Но можно явно передать файловый объект для печати в файл. Для этого
надо воспользоваться ключевым параметром file.
"""

text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)
