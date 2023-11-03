from typing import Generator


def primes(left: int, right: int) -> Generator:
    for i in range(left, right + 1):
        flag = True
        for j in range(2, i):
            if not i % j:
                flag = False
        if flag is True and i != 1:
            yield i
