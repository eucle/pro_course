import csv

res_d: dict = {}
with open('salary_data.csv', 'r', encoding='utf-8') as csv_file:
    rows = csv.DictReader(csv_file, delimiter=';')
    for row in rows:
        res_d[row['company_name']] = \
           res_d.get(row['company_name'], [0]) + [int(row['salary'])]
        res_d[row['company_name']][0] += 1
    for item in sorted(res_d.items(), key=lambda x: sum(x[1][1:]) / x[1][0]):
        print(item[0])
