'''
Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt
'''

fileref = open("emotion_words2.txt", "r")
first_forty = fileref.read(40)
print(first_forty)
fileref.close()