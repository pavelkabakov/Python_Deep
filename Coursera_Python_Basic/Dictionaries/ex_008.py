"""
Create a dictionary named `letter_counts` that contains each letter and the number of times it occurs in `string1`.

**Challenge:** Letters should not be counted separately as upper-case and lower-case.

Intead, all of them should be counted as lower-case.

"""

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}

for one_char in string1.lower():
    if one_char not in letter_counts:
        letter_counts[one_char] = 0
    letter_counts[one_char] = letter_counts[one_char] + 1
print(letter_counts)