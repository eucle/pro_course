import csv
from datetime import datetime as dt


dictio: dict = {}
with open('name_log.csv', 'r', encoding='utf-8') as file:
    rows = [[a, b, dt.strptime(c, '%d/%m/%Y %H:%M')]
            for a, b, c in list(csv.reader(file))[1:]]

    for row in sorted(rows, key=lambda x: (x[1], x[2])):
        if row[1] not in dictio or dictio[row[1]][1] < row[2]:
            dictio[row[1]] = [row[0], row[2]]

with open('new_name_log.csv', 'w', encoding='utf-8') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['username', 'email', 'dtime'])
    for key, value in dictio.items():
        writer.writerow([value[0],
                         key, dt.strftime(value[1], '%d/%m/%Y %H:%M')])
