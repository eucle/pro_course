import time


def for_and_append(iterable):
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):
    return [elem for elem in iterable]


def list_function(iterable):
    return list(iterable)


funcs = [for_and_append, list_comprehension, list_function]
iterable = range(100_000)


def get_the_fastest_func(funcs, iterable):

    times = []
    for func in funcs:
        start = time.perf_counter_ns()
        func(iterable)
        end = time.perf_counter_ns()
        times.append(end - start)
    print(times)
    return funcs[times.index(min(times))]


print(get_the_fastest_func(funcs, iterable))
