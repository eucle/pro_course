import csv


with open('data.csv', 'r', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter='@'))

dictio: dict = {}
for row in rows[1:]:
    dictio[row[1]] = dictio.get(row[1], 0) + 1

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['domain', 'count'])
    for item in sorted(dictio.items(), key=lambda x: (x[1], x)):
        writer.writerow(item)
