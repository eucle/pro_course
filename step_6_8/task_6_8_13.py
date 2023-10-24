from collections import Counter


most_tuple = Counter(map(str.lower, input().split())).most_common()
most_sorted = sorted(filter(lambda x: x[1] == most_tuple[-1][1], most_tuple))
print(', '.join([el[0] for el in most_sorted]))
