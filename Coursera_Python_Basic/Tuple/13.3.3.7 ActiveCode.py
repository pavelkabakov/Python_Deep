#from Coursera_Python_Basic.files.ex_011_write_to_file import number

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
print(pokemon.items())
p_names = []
p_number = []
for item in (pokemon.items()):
    names, number = item
    p_names.append(names)
    p_number.append(number)
    print(item)