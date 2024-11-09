olympicsfile = open("olympics.txt", "r")

for aline in olympicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()