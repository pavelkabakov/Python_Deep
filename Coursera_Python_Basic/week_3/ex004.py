'''
Напишите код, который подсчитывает количество слов в sentence которые содержат либо букву “а", либо букву “е". Сохраните результат в переменной num_a_or_e.

Примечание 1: не учитывайте дважды слова, в которых есть и буква «а», и буква «е».

ПОДСКАЗКА 1: используйте оператор in.

ПОДСКАЗКА 2: Вы можете использовать or или elif.

Жестко заданные ответы не будут засчитаны.
'''

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

num_a_or_e = 0
sentence_list = sentence.split(" ")
for num in sentence_list:
    if "a" in num or "e" in num:
        num_a_or_e += 1

print(num_a_or_e)