import time


funcs = [print, bin, round, abs]
arg = -100_000_000_000 ** 2


def get_the_fastest_func(funcs, arg):

    times = []
    for func in funcs:
        start = time.perf_counter_ns()
        func(arg)
        end = time.perf_counter_ns()
        times.append(end - start)
    return funcs[times.index(min(times))]


print(get_the_fastest_func(funcs, arg))
