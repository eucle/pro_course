import csv
import json


addresses: dict = {}
with open('playgrounds.csv', 'r', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=";"))[1:]
    for _, district, area, address in rows:
        addresses.setdefault(district, {})
        addresses[district][area] = (
            addresses[district].get(area, []) + [address]
        )

with open('addresses.json', 'w', encoding='utf-8') as out_file:
    json.dump(addresses, out_file, indent=3, ensure_ascii=False)
