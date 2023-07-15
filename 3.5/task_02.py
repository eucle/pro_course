from datetime import date


res: dict = {}
for d in range(5, date.max.toordinal()):
    if date.fromordinal(d).day == 13:
        key = date.fromordinal(d).isoweekday()
        res[key] = res.get(key, 0) + 1
for key in sorted(res):
    print(res[key])
