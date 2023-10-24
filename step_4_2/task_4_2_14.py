import csv


u_input = int(input()) - 1
with open('deniro.csv', 'r', encoding='utf-8') as csv_f:
    rows: map = map(lambda x: [x[0], int(x[1]), int(x[2])], csv.reader(csv_f))
    for a, b, c in sorted(rows, key=lambda x: x[u_input]):
        print(f'{a}, {b}, {c}')
