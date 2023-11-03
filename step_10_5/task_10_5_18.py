from typing import Generator, Iterable


def reverse(sequence: Iterable) -> Generator:
    for elem in reversed(sequence):
        yield elem
