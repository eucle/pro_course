import csv
from collections import namedtuple
from datetime import datetime as dt


Guest = namedtuple('Guest', ['surname', 'name', 'dt_tm'])

guests = []
with open('meetings.csv', mode='r', encoding='utf-8') as file:
    for sn, n, *d_t in csv.reader(list(file)[1:]):
        guest = Guest(sn, n, dt.strptime(' '.join(d_t), '%d.%m.%Y %H:%M'))
        guests.append(guest)

guests.sort(key=lambda x: x.dt_tm)
print(*[f'{g.surname} {g.name}' for g in guests], sep='\n')
