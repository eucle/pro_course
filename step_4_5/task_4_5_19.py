from zipfile import ZipFile


file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf']
with ZipFile('files.zip', 'w') as zip_file:
    for file in file_names:
        zip_file.write(file)
