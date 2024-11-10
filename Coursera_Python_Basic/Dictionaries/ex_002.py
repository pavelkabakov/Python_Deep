"""
Create a dictionary, `freq`, that displays each character in string `str1` as the key and its frequency as the value.
"""

str1 = 'peter piper picked a peck of pickled peppers'
freq = {}

for one_char in str1:
    if one_char not in freq:
        freq[one_char] = 0
    freq[one_char] = freq[one_char] + 1
print(freq)

