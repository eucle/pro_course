from random import randrange


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.iterator = iter([randrange(left, right + 1) for _ in range(n)])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            raise
