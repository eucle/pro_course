import sys
import json


data = sys.stdin.read()
for key, value in json.loads(data).items():
    if type(value) == list:
        value = list(map(str, value))
    print(f'{key}: {", ".join(value) if type(value) == list else value}')
