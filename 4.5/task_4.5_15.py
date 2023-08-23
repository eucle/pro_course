from zipfile import ZipFile


res: dict = {}
with ZipFile('workbook.zip') as zip_file:
    for obj in zip_file.infolist():
        res['file_size'] = res.get('file_size', 0) + obj.file_size
        res['compress_size'] = res.get('compress_size', 0) + obj.compress_size

print(f'Объем исходных файлов: {res["file_size"]} байт(а)')
print(f'Объем сжатых файлов: {res["compress_size"]} байт(а)')
