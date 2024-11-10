sentence = "The dog chased the rabbit. The rabbit hopped into the bushes."
words = sentence.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)
