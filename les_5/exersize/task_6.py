data = [2, 4, 6, 8, 10, ]

for item in data:
    print(item, end='\t')

# аналогичная операция в одну строку с распаковкой:
print('\n')
print(*data, sep='\t')