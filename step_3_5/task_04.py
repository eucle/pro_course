from datetime import date, datetime, timedelta


start, end = [datetime.strptime(input(), '%d.%m.%Y') for _ in '12']
while not (start.day + start.month) % 2:
    start += timedelta(days=1)
for d in range(start.toordinal(), end.toordinal() + 1, 3):
    if date.fromordinal(d).weekday() not in (0, 3):
        print(date.fromordinal(d).strftime('%d.%m.%Y'))
