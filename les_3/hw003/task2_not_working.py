import string

text = 'Hello world. Hello Python. Hello again.'

def top_ten_words(text):
    # Преобразуем текст в нижний регистр
    text = text.lower()
    # Удаляем знаки препинания
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Разбиваем текст на слова
    words = text.split()

    # Подсчитываем встречаемость каждого слова
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    # Сортируем слова по частоте в убывающем порядке, а при равной частоте - по убыванию алфавитного порядка
    sorted_words = sorted(word_count.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

    # Возвращаем первые 10 слов, если в списке меньше 10 слов, возвращаем их все
    return sorted_words

# Пример использования

print(top_ten_words(text))
