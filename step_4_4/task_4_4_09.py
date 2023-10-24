import json


with open('people.json', 'r', encoding='utf-8') as input_f:
    people_list = json.load(input_f)
    person_with_max_keys = max(people_list, key=len)

for person in people_list:
    for key in person_with_max_keys:
        person[key] = person.get(key, None)

with open('updated_people.json', 'w', encoding='utf-8') as output_f:
    json.dump(people_list, output_f, indent=3)
