import time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


def calculate_it(func, *args):
    start_time = time.perf_counter()

    res = func(*args)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    return res, elapsed_time


print(calculate_it(add, 1, 2, 3))
