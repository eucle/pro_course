from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name, mode='r') as zip_file:
        if not args:
            zip_file.extractall()
        else:
            list(map(zip_file.extract, args))


extract_this('workbook.zip', 'second_image.jpg')
