"""
Provided is a string saved to the variable name `s1`. Create a dictionary named `counts` that contains each letter
 in `s1` and the number of times it occurs.
"""
s1 = 'hello'
counts = {}

for one_char in s1:
    if one_char not in counts:
        counts[one_char] = 0
    counts[one_char] = counts[one_char] + 1
print(counts)