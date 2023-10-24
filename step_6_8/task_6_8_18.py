import csv

from collections import Counter


with open('name_log.csv', mode='r', encoding='utf-8') as file:
    emails = [row[1] for row in csv.reader(list(file)[1:])]

res = sorted(Counter(emails).items())
[print(f'{k}: {v}') for k, v in res]
