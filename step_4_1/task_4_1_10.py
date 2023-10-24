import sys


data = sys.stdin.readlines()
for txt in data:
    print(txt.strip()[::-1])
