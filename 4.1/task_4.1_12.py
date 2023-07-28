import sys


res = [int(line.strip()) for line in sys.stdin]
print('Анри' if (len(res) % 2 and not res[-1] % 2) or
      (not len(res) % 2 and res[-1] % 2) else 'Дима')
