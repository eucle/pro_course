from collections import Counter


print(Counter(map(str.lower, input().split())).most_common(1)[0][0])
