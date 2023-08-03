import csv


def csv_columns(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        dictio = {}
        rows = tuple(csv.reader(csv_file))
        for row in rows[1:]:
            for i in range(len(row)):
                dictio[rows[0][i]] = dictio.get(rows[0][i], []) + [row[i]]
        return dictio


print(csv_columns('data.csv'))
