import csv
import json


with open('students.json', 'r', encoding='utf-8') as file:
    stdnts = [(st['name'], st['phone']) for st in json.load(file)
              if st['age'] > 17 and st['progress'] > 74]
    stdnts.sort()

with open('data.csv', 'w', encoding='utf-8') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['name', 'phone'])
    writer.writerows(stdnts)
