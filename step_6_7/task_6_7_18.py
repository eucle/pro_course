from collections import Counter


goods = Counter(input().split(','))
max_len = len(max(goods.keys(), key=len))
for key, val in sorted(goods.items()):
    price = sum(ord(letter) for letter in key if letter.isalpha())
    print(f'{key + " " * (max_len - len(key))}: '
          f'{price} UC x {val} = {price * val} UC')
