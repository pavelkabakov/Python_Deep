# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

text = ' Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.'


def sort_words(my_text):
    return sorted(set([ord(ch) for ch in my_text]), reverse=True)


print(sort_words(text))
