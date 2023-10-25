from random import randrange


def random_numbers(left, right):
    return iter(lambda: randrange(left, right + 1), right + 1)
