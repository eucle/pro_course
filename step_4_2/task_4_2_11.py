import csv


with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    writer.writeheader()
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})
