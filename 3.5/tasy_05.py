from datetime import datetime
from typing import Any


employees: Any = [input().split() for _ in range(int(input()))]
for employee in employees:
    employee[2] = datetime.strptime(employee[2], '%d.%m.%Y')
max_age = min(employees, key=lambda x: x[2])[2]
aged_emps = list(filter(lambda x: x[2] == max_age, employees))
if len(aged_emps) > 1:
    print(f"{datetime.strftime(max_age, '%d.%m.%Y')} {len(aged_emps)}")
else:
    print(f"{datetime.strftime(max_age, '%d.%m.%Y')} {aged_emps[0][0]} {aged_emps[0][1]}")
