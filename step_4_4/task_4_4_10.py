import json


with open('countries.json', 'r', encoding='utf-8') as input_file:
    objects = json.load(input_file)

religion_list: dict = {}
for obj in objects:
    religion_list[obj['religion']] = (religion_list.get(obj['religion'], []) +
                                      [obj['country']])

with open('religion.json', 'w', encoding='utf-8') as output_file:
    json.dump(religion_list, output_file, indent=3)
