from datetime import date


dates = list(map(lambda x: date(*list(map(int, x.split('.')[::-1]))), input().split()))
print([abs(dates[i + 1] - dates[i]).days for i in range(len(dates) - 1)])
