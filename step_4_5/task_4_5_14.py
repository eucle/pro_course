from zipfile import ZipFile


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
print(sum([not obj.is_dir() for obj in info]))
