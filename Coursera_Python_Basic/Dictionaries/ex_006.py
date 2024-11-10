"""
Create the dictionary `characters` that shows each character from the string `sally` and its frequency.
 Then, find the most frequent letter based on the dictionary.
  Assign this letter to the variable `best_char`.
"""
sally = 'sally sells sea shells by the sea shore oooooooooooooooooooooooo'
characters = {}


for one_char in sally:
    if one_char not in characters:
        characters[one_char] = 0
    characters[one_char] = characters[one_char] + 1
print(characters)

best_char = sally[0]
print(best_char)

for key in characters:
    if characters[best_char] < characters[key]:
        best_char = key
print(best_char)