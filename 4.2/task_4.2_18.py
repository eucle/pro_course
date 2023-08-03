import csv


male: list = []
female: list = []
with open('titanic.csv', 'r', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=';'))
    for row in filter(lambda x: x[0] != '0' and int(float(x[3])) < 18, rows[1:]):
        male.append(row[1]) if row[2] == 'male' else female.append(row[1])
print(*male, sep='\n')
print(*female, sep='\n')
