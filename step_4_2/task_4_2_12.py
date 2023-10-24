import csv


with open('sales.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')
    for row in rows:
        if int(row['old_price']) > int(row['new_price']):
            print(row['name'])
