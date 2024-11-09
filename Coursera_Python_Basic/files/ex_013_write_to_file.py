file_name = "school_prompt3.txt"
file_ref = open(file_name, 'w')
for num in range (1, 20):
    file_ref.write(str(num) + "\n")
file_ref.close()

file_ref = open(file_name, 'r')
for str in file_ref:
    print(str.strip())
file_ref.close()



