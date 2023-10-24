import sys


print(sum([line.strip()[0] == '#' for line in sys.stdin]))
