from zipfile import ZipFile
from datetime import datetime as dt


files = []
with ZipFile('workbook.zip') as zip_file:
    for obj in zip_file.infolist():
        if not obj.is_dir():
            files.append((obj.filename.split('/')[-1],
                          obj.date_time,
                          obj.file_size,
                          obj.compress_size))

files.sort()
for file in files:
    print(f'{file[0]}\n  Дата модификации файла: {dt(*file[1])}')
    print(f'  Объем исходного файла: {file[2]} байт(а)')
    print(f'  Объем сжатого файла: {file[3]} байт(а)\n')
