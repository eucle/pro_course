import csv


with open('titanic.csv', 'r', encoding='utf-8') as file:
    chosen = [data for stat, *data, age in
              tuple(csv.reader(file, delimiter=';'))[1:]
              if stat != '0' and float(age) < 18]
    [print(pers[0]) for pers in
     sorted(chosen, key=lambda x: x[1], reverse=True)]
