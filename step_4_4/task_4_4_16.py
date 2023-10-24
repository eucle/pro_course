import json


objects: dict = {}
with open('food_services.json', 'r', encoding='utf-8') as in_file:
    for place in json.load(in_file):
        objects[place['TypeObject']] = (objects.get(place['TypeObject'], []) +
                                        [(place['Name'], place['SeatsCount'])])

for key, value in sorted(objects.items()):
    max_value = max(value, key=lambda x: x[1])
    print(f'{key}: {max_value[0]}, {max_value[1]}', sep='\n')
