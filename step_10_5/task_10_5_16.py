def alternating_sequence(count=None):
    num = 1
    while (num <= count) if type(count) is int else True:
        yield num * (-1, 1)[num % 2]
        num += 1
