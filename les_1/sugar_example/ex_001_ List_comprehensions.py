"""
Без синтаксического сахара:
"""

numbers = [1, 2, 3, 4, 5]
squared = []
for number in numbers:
    squared.append(number ** 2)

print(squared)

"""
С синтаксическим сахаром:
"""

squared2 = [number ** 2 for number in numbers]
print(squared2)
