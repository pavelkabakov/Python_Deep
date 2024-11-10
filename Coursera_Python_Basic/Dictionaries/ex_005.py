"""
Create a dictionary called `wrd_d` from the string `sent`, so that the key is a word and the value is how many times you have seen that word.
"""
sent = 'Singing in the rain and playing in the rain are two entirely different situations but both can be good'
wrd_d = {}
words_list = sent.split()

for one_word in words_list:
    if one_word not in wrd_d:
        wrd_d[one_word] = 0
    wrd_d[one_word] = wrd_d[one_word] + 1
print(wrd_d)