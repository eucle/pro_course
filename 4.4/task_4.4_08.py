import json


with open('data1.json', 'r', encoding='utf-8') as data1,\
     open('data2.json', 'r', encoding='utf-8') as data2:
    alldata = json.load(data1) | json.load(data2)

with open('data_merge.json', 'w', encoding='utf-8') as output:
    json.dump(alldata, output, indent=3)
