import json


dists: dict = {}
comps: dict = {}
with open('food_services.json', 'r', encoding='utf-8') as in_file:
    for obj in json.load(in_file):
        dists[obj['District']] = dists.get(obj['District'], 0) + 1
        if obj['OperatingCompany']:
            comps[obj['OperatingCompany']] = comps.get(obj['OperatingCompany'], 0) + 1

max_dists = max(dists.items(), key=lambda x: x[1])
max_comps = max(comps.items(), key=lambda x: x[1])
print(f'{max_dists[0]}: {max_dists[1]}')
print(f'{max_comps[0]}: {max_comps[1]}')
