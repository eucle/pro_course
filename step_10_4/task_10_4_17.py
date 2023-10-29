class Xrange:
    def __init__(self, start, end, step=1):
        self.cnt = start - step
        self.end = end - step
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.cnt >= self.end
                or self.step < 0 and self.cnt <= self.end):
            raise StopIteration
        self.cnt += self.step
        return self.cnt
