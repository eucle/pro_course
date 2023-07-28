from datetime import datetime as dt
import sys


res = [dt.strptime(line.strip(), '%Y-%m-%d') for line in sys.stdin]
print((max(res) - min(res)).days)
