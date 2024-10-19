'''
Найти самый длинный строчный экземпляр в предложенном массиве:
'''

array = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipisicing', 'elit.', 'Ducimus', 'pariatur', 'veniam', 'nisi', 'consectetur', 'maxime', 'harum',
         'a,', 'tempora', 'consequatur', 'animi', 'eos,', 'soluta?', 'Eum', 'magni', 'reiciendis,', 'omnis?', 'Officia', 'molestiae', 'in,', 'nemo', 'nihil.']

print(array)
max_len = 0

for index, str1 in enumerate(array):
    if len(str1) > max_len:
        max_len = len(str1)

print(f"max length = {max_len}")
print('elements with max length:')

for index, str1 in enumerate(array):
    if len(str1) == max_len:
        print(f'index: {index}, string: {str1}, length:{len(str1)}')
