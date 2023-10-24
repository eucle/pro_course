import json


with open('data.json', 'r', encoding='utf-8') as obj:
    res = []
    for el in json.load(obj):
        if el is None:
            pass
        else:
            if isinstance(el, str):
                el += '!'
            elif isinstance(el, bool):
                el = bool(el < 1)
            elif isinstance(el, int):
                el += 1
            elif isinstance(el, list):
                el *= 2
            elif isinstance(el, dict):
                el["newkey"] = None
            res.append(el)

with open('updated_data.json', 'w', encoding='utf-8') as obj:
    json.dump(res, obj, indent=3)
