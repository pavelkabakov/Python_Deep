'''
Напишите код, который использует строку, хранящуюся в org и создаёт аббревиатуру, которая присваивается переменной acro.
 Следует использовать только первую букву каждого слова, каждая буква в аббревиатуре должна быть заглавной,
  и между буквами аббревиатуры не должно быть пробелов. Слова, которые не должны входить в аббревиатуру,
   хранятся в списке stopwords. Например, если org присвоена строка «приветствую мир»,
   то в результате должна получиться аббревиатура «HW».
'''

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
temp_str = org.lower()
print(temp_str)
my_list = temp_str.split(" ")
acro=""
print(my_list)
print(stopwords)
for my_word in my_list:
        if my_word not in stopwords:
            acro += str(my_word[0]).upper()
            print(acro)
print(acro)
