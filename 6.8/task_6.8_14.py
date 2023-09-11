from collections import Counter


counter = Counter(input().lower().split()).most_common()
print(max(counter, key=lambda x: (x[1], x[0]))[0])
