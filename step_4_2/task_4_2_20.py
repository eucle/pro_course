import csv


def condense_csv(csv_file, id_name):
    with open(csv_file, 'r', encoding='utf-8') as file:
        rows = list(csv.reader(file))

    columns = [id_name]
    counter = 0
    cell = rows[0][0]
    while cell == rows[0][0]:
        columns.append(rows[counter][1])
        counter += 1
        cell = rows[counter][0]

    cell = rows[0][0]
    line = []
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(columns)
        for row in rows:
            if not line:
                line.append(row[0])
                line.append(row[2])
            elif line[0] == row[0]:
                line.append(row[2])
            else:
                writer.writerow(line)
                line.clear()
                line.append(row[0])
                line.append(row[2])
        writer.writerow(line)


print(condense_csv('data.csv', 'ID'))
