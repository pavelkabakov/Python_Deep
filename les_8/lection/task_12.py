"""
Если передать список строк в параметр fieldnames, они будут использоваться для
ключей словаря, а не первая строка файла. В нашем примере передан “лишний”
ключ count. Т.к. в таблице нет шестого столбца, ему было присвоено значение из
параметра restval.
"""

import csv
with open('biostats_tab.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office",
                              dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
        print(f'{line["name"] = }\t{line["age"] = }')