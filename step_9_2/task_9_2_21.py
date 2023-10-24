from sys import stdin

res = 0
for line in stdin:
    res = max(res, eval(line))
