from datetime import datetime


def conv_time(time_tuple):
    start = datetime.strptime(time_tuple[0], '%H:%M')
    finish = datetime.strptime(time_tuple[1], '%H:%M')
    return start.time(), finish.time()


w = [('09:00', '21:00')] * 5 + [('10:00', '18:00')] * 2
user_d = datetime.strptime(input(), '%d.%m.%Y %H:%M')
user_d_weekday = user_d.weekday()
if user_d.time() >= conv_time(w[user_d_weekday])[0] and \
   user_d.time() < conv_time(w[user_d_weekday])[1]:
    print(int((datetime.combine(user_d.date(), conv_time(w[user_d_weekday])[1]) - user_d).seconds / 60))
else:
    print('Магазин не работает')
