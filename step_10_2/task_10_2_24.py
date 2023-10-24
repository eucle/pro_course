from typing import Iterator


def get_min_max(iterable):
    mini = None
    maxi = None
    if isinstance(iterable, Iterator):
        while True:
            try:
                value = next(iterable)
                if mini is None:
                    if type(value) is str:
                        mini = 'a'
                        maxi = 'a'
                        res = [value] + list(iterable)
                        res.sort()
                        return res[0], res[-1]
                    else:
                        mini = value
                        maxi = 0

                if value > maxi:
                    maxi = value
                else:
                    mini = min(mini, value)
            except StopIteration:
                break
        if maxi:
            return mini, maxi
    elif iterable:
        return min(iterable), max(iterable)
