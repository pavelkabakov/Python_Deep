fileref = open("olympics.txt", "r")
## other code here that refers to variable fileref
for str in fileref:
    print(str.strip())
    # print(str)
fileref.close()