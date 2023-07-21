from calendar import month, month_abbr

y, m = input().split()
print(month(int(y), list(month_abbr).index(m)))
