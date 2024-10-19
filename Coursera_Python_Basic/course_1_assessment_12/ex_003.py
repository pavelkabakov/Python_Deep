'''
Напишите код, который использует строку, хранящуюся в sent и создает сокращение, которое присваивается переменной acro. Должны использоваться первые две буквы
 каждого слова, каждая буква в аббревиатуре должна быть заглавной, а каждый элемент аббревиатуры должен разделяться знаком “. “ (точка и пробел).
 Слова, которые не должны быть включены в аббревиатуру, сохраняются в списке stopwords. Например, если sent была присвоена строка “height and ewok wonder”,
  то результирующая аббревиатура должна быть “HE. EW. WO”.
'''

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

temp_str = sent.lower()
print(temp_str)
my_list = temp_str.split(" ")
acro_list = []
acro=""
print(my_list)
print(stopwords)
for my_word in my_list:
        if my_word not in stopwords:
            acro_list.append(str(my_word[0]).upper() + str(my_word[1]).upper())
            print(acro)
acro = ". ".join(acro_list)
print(acro_list)
print(acro)