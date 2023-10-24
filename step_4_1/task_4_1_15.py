import sys


print(*[line for line in sys.stdin if not line.strip().startswith('#')], sep="")
