from datetime import datetime


pattern, empls = '%d.%m.%Y', {}
curr_d = datetime.strptime(input(), pattern)
for _ in range(int(input())):
    empl: list = input().rsplit(' ', 1)
    empl[1] = datetime.strptime(empl[1], pattern)
    if 0 < (empl[1].replace(year=1) - curr_d.replace(year=1)).days < 8 or \
       -358 > (empl[1].replace(year=1) - curr_d.replace(year=1)).days > -365:
        empls[empl[1]] = empl[0]
if empls:
    print(empls[max(empls)])
else:
    print("Дни рождения не планируются")
