'''
Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
'''

fileref = open("travel_plans2.txt", "r")
num_lines = 0
for str in fileref:
    print(str)
    num_lines += 1

print(num_lines)
fileref.close()