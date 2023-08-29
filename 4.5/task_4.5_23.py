from zipfile import ZipFile


def converting_units(file_size):
    if file_size / 1_024 < 1:
        return f' {file_size} B'
    elif 1_024 > file_size / 1_024 > 0:
        return f' {round(file_size / 1024)} KB'
    elif 1_024 > file_size / 1_048_576 > 0:
        return f' {round(file_size / 1_048_576)} MB'
    elif 1_024 > file_size / 1_073_741_824 > 0:
        return f' {round(file_size / 1_073_741_824)} GB'


with ZipFile('desktop.zip') as zip_file:
    for obj in zip_file.infolist():
        splitted_obj = obj.filename.rstrip('/').split('/')
        print(f'{(len(splitted_obj) - 1) * "  "}{splitted_obj[-1]}', end='')
        print(f'{(converting_units(obj.file_size), "")[obj.is_dir()]}')
