from collections import Counter
from sys import stdin


dictio: dict = {}
for item in stdin:
    name, rating = item.split()
    dictio[name] = int(rating)
students = Counter(dictio)

print(students.most_common()[-2][0])
