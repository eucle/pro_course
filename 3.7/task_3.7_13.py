from calendar import monthrange as mr, weekday as wd
from datetime import date


def get_all_mondays(year):
    return [date(year, m, d)
            for m in range(1, 13)
            for d in range(1, mr(year, m)[1] + 1)
            if not wd(year, m, d)]


print(get_all_mondays(2077))
