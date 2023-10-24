import csv
from typing import Any


with open('student_counts.csv', 'r', encoding='utf-8') as file:
    rows: Any = csv.DictReader(file, delimiter=',')
    columns = ['year'] +\
        sorted(rows.fieldnames[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[-1]))
    new_rows: list = list(rows)

with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=',')
    writer.writeheader()
    for row in new_rows:
        writer.writerow(row)
