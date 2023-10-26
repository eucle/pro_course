class Square:
    def __init__(self, n):
        self.n = n
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1
        if self.cnt > self.n:
            raise StopIteration
        return self.cnt * self.cnt
