from datetime import datetime


def choose_plural(amount: int, declensions: tuple) -> str:
    last_nums = str(amount)[-2:]
    if int(last_nums[-1]) == 1 and int(last_nums) - 10 != 1:
        return f'{amount} {declensions[0]}'
    elif 1 < int(last_nums[-1]) < 5 and int(last_nums) - 10 not in range(2, 5):
        return f'{amount} {declensions[1]}'
    return f'{amount} {declensions[2]}'


units = {'days': ('день', 'дня', 'дней'),
         'hours': ('час', 'часа', 'часов'),
         'mins': ('минута', 'минуты', 'минут'),
         }
release_d = datetime(2022, 11, 8, 12)
current_d = datetime.strptime(input(), '%d.%m.%Y %H:%M')
if current_d >= release_d:
    print('Курс уже вышел!')
else:
    residue = release_d - current_d
    res_days, res_hours, res_mins = residue.days, int(residue.seconds / 3600), (residue.seconds // 60) % 60
    if res_days:
        if res_hours >= 1:
            print(f"До выхода курса осталось: {choose_plural(res_days, units['days'])} и {choose_plural(res_hours, units['hours'])}")
        else:
            print(f"До выхода курса осталось: {choose_plural(res_days, units['days'])}")
    else:
        if res_hours >= 1:
            if res_mins >= 1:
                print(f"До выхода курса осталось: {choose_plural(res_hours, units['hours'])} и {choose_plural(res_mins, units['mins'])}")
            else:
                print(f"До выхода курса осталось: {choose_plural(res_hours, units['hours'])}")
        else:
            print(f"До выхода курса осталось: {choose_plural(res_mins, units['mins'])}")
