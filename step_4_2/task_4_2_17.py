import csv


with open('wifi.csv', 'r', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=';'))[1:]
    dictio: dict = {}
    for row in rows:
        dictio[row[1]] = dictio.get(row[1], 0) + int(row[3])
    for item in sorted(dictio.items(), key=lambda x: (-x[1], x)):
        print(f'{item[0]}: {item[1]}')
