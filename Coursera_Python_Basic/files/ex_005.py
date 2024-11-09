'''
Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
'''

fileref = open("school_prompt2.txt", "r")
num_char = len(fileref.read())
print(num_char)
fileref.close()