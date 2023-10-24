from collections import Counter


def isalph(symbol: str) -> bool:
    return symbol.isalpha()


with open('pythonzen.txt', mode='r', encoding='utf-8') as f:
    res = Counter(filter(isalph, map(str.lower, f.read().replace('\n', ''))))
    [print(f'{key}: {val}') for key, val in sorted(res.items())]
