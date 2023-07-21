import time
from math import factorial                   # функция из модуля math


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


funcs = [factorial, factorial_classic, factorial_recurrent]
arg = 900


def get_the_fastest_func(funcs, arg):

    times = []
    for func in funcs:
        start = time.perf_counter_ns()
        func(arg)
        end = time.perf_counter_ns()
        times.append(end - start)
    return funcs[times.index(min(times))]


print(get_the_fastest_func(funcs, arg))
