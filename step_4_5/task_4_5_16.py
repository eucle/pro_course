from zipfile import ZipFile


with ZipFile('workbook.zip') as zip_file:
    res = {(obj.filename, (obj.compress_size / obj.file_size) * 100)
           for obj in zip_file.infolist() if not obj.is_dir()}

file_name = min(res, key=lambda x: x[1])[0]
print(file_name[file_name.index('/') + 1:])
