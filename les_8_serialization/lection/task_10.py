"""
Запись CSV
"""

import csv

with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for i, line in enumerate(csv_read):
        if i == 0:
            csv_write.writerow(line)
        else:
            line[2] += 1
            for j in range(2, 4 + 1):
                line[j] = int(line[j])
            all_data.append(line)
    csv_write.writerows(all_data)


"""
import csv

# Открываем файлы в отдельных контекстных менеджерах
with open('biostats_tab.csv', 'r', newline='') as f_read:
    csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
    all_data = []
    for i, line in enumerate(csv_read):
        if i > 0:  # Пропускаем заголовок
            # Преобразуем нужные значения в int
            line[2] = int(line[2]) + 1  # Увеличиваем возраст
            for j in range(2, 4 + 1):
                line[j] = int(line[j])
            all_data.append(line)
        else:
            header = line  # Сохраняем заголовок

# Открываем файл для записи
with open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_write.writerow(header)  # Записываем заголовок
    csv_write.writerows(all_data)  # Записываем обработанные данные
"""

