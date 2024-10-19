'''
Палиндром — это фраза, которая, если её прочитать задом наперёд, будет читаться так же. Напишите код, который проверяет,
 является ли p_phrase палиндромом, переворачивая его и затем проверяя, совпадает ли перевёрнутая версия с исходной.
  Присвойте перевёрнутую версию p_phrase переменной r_phrase, чтобы мы могли проверить вашу работу.
'''

p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
temp_str1 = p_phrase.lower().replace(' ', '')
temp_str2 = r_phrase.lower().replace(' ', '')
print(temp_str1)
print(temp_str2)

for i in range(len(temp_str1)):

    if temp_str1[i] != temp_str2[i]:
       print('is not pallindrom')
       break



