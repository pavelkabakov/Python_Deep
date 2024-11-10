"""
Find the least frequent letter. Create the dictionary `characters` that shows each character from string `sally`
and its frequency.
Then, find the least frequent letter in the string and assign the letter to the variable `worst_char`.
"""

sally = 'sally sells sea shells by the sea shore and by the road'
# sally_no_spaces = sally.replace(' ', '')
characters = {}

worst_char = sally[0]

for one_char in sally:
    if one_char not in characters:
        characters[one_char] = 0
    characters[one_char] = characters[one_char] + 1
print(characters)

for key in characters:

    if characters[worst_char] > characters[key]:
        # print(f'the key is: "{key}" if {characters[worst_char]} < {characters[key]} ')
        worst_char = key

print(f'worst_char = "{worst_char}"')

