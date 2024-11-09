'''
md = open('mydata.txt', 'r')
for line in md:
    print(line)
md.close()
# continue with other code
эквивалентный код ниже
'''


with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
# continue on with other code