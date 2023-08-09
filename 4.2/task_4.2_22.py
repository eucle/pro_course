import csv
from typing import Any


res: list[Any] = []
with open('prices.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    for row in list(rows)[1:]:
        min_price = min(row[1:], key=lambda x: int(x))
        ind_min_price = row.index(min_price)
        res.append([row[0], int(min_price), ind_min_price])

shop = min(res, key=lambda x: x[1])
print(f'{rows[0][shop[2]]}: {shop[0]}')
