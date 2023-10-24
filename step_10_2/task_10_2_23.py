def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)
