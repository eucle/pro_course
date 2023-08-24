from zipfile import ZipFile
import os.path as o_p


f_list = ['test1.txt',
          'test2.txt',
          'test3.txt']

with ZipFile('new_file.zip', mode='a') as zip_file:
    list(map(zip_file.write, filter(lambda x: o_p.getsize(x) < 101, f_list)))
