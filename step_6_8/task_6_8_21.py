import csv
import json

from collections import Counter


result_dict: Counter = Counter()
res: int = 0

for num in '1234':
    with open('quarter' + num + '.csv', mode='r', encoding='utf-8') as file:
        data = csv.reader(list(file)[1:])
    dictio = Counter({prod: sum(map(int, kgs)) for prod, *kgs in data})
    result_dict += dictio

with open('prices.json', mode='r', encoding='utf-8') as file:
    for kilos, price in zip(result_dict.values(), json.load(file).values()):
        res += kilos * price

print(res)
