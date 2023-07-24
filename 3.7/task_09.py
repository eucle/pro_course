import calendar


num = calendar.weekday(*map(int, input().split('-')))
print(list(calendar.day_name)[num])
