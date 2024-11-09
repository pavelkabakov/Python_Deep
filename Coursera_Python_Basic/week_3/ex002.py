'''
Переменная sentence хранит строку. Напишите код, который определит, сколько слов в sentence начинаются и заканчиваются одной и той же буквой, включая однобуквенные слова. Сохраните результат в переменной same_letter_count.

Жестко заданные ответы не будут засчитаны.
'''

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
list_words = sentence.split(" ")
same_letter_count = 0
print(list_words)
for word in list_words:
    if word[0] == word[-1] and len(word) > 1:
        print(word)
        same_letter_count += 1

print(same_letter_count)