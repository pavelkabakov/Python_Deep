# Напишите функцию на Python, которая принимает строку и возвращает количество гласных букв в этой строке.

s = "Hello World"

def count_vowels(str):
    count = 0
    vowels = set("aeiou")
    for letter in str:
        if letter in vowels:
            count += 1
    return count

print("Количество гласных равно:")
print(count_vowels(s))