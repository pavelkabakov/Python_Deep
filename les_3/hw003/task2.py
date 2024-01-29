import string

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
        if word.isdigit():
            continue
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Сортируем слова по частоте в убывающем порядке и для одинаковой частоты - в обратном алфавитном порядке
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    # Возвращаем первые 10 слов
    return sorted_words[:10]

# Пример использования
text = 'Hello world. Hello Python. Hello again.'
print(top_ten_words(text))
