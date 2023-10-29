class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.length = len(iterable)
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt == self.length:
            self.cnt = 0
        val = self.iterable[self.cnt]
        self.cnt += 1
        return val
