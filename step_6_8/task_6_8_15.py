from collections import Counter


words = Counter([len(word) for word in input().split()])
for k, v in sorted(words.items(), key=lambda x: x[1]):
    print(f'Слов длины {k}: {v}')
