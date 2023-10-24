from collections import Counter


res = 0
dictio = Counter(input().split())
for i in range(int(input())):
    book, price = input().split()
    if book in dictio:
        dictio -= Counter({book: 1})
        res += int(price)

print(res)
