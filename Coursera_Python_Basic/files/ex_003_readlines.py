fileref = open("olympics.txt", "r")
## other code here that refers to variable fileref
# for str in fileref:
#     print(str.strip())
for srting in fileref.readlines():
    print(srting)
print(fileref.readlines())
fileref.close()