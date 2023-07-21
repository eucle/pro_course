import time


def for_and_append():
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


funcs = [for_and_append, list_comprehension]


def get_the_fastest_func(funcs):

    times = []
    for func in funcs:
        start = time.perf_counter_ns()
        func()
        end = time.perf_counter_ns()
        times.append(end - start)
    print(times)
    return funcs[times.index(min(times))]


print(get_the_fastest_func(funcs))
