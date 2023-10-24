from datetime import date, datetime, timedelta


def fill_up_missing_dates(dates: list) -> list:
    pattern = '%d.%m.%Y'
    new_d = list(map(lambda x: datetime.strptime(x, pattern), dates))
    mi = min(new_d)
    return [date.strftime(mi + timedelta(days=i), pattern) for i in range((max(new_d) - mi).days + 1)]


dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))
