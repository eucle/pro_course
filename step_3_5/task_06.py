from datetime import datetime


bds: dict = {}
for _ in range(int(input())):
    bd = datetime.strptime(input().split()[2], '%d.%m.%Y')
    bds[bd] = bds.get(bd, 0) + 1
pop_date = max(bds.values())
for key, value in sorted(bds.items()):
    if value == pop_date:
        print(datetime.strftime(key, '%d.%m.%Y'))
