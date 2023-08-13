import json


def is_correct_json(string):
    try:
        return bool(json.loads(string))
    except json.decoder.JSONDecodeError:
        return False


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))
