"""
Create a dictionary, `freq_words`, that contains each word in string `str1` as the key and its frequency as the value.
"""

str1 = 'I wish I wish with all my heart to fly with dragons in a land apart'
freq_words = {}
words_list = str1.split()

for one_word in words_list:
    if one_word not in freq_words:
        freq_words[one_word] = 0
    freq_words[one_word] = freq_words[one_word] + 1
print(freq_words)