"""
Ниже приведён набор оценок, которые студенты получили за прошлый семестр. Напишите код, чтобы определить,
 сколько оценок равно 90 или выше, и присвойте этот результат значению a_scores.
"""

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
my_list = list(map(int, scores.split(" ")))
a_scores = 0
print(my_list)
for grade in my_list:
    if grade >= 90:
        a_scores += 1
print(a_scores)