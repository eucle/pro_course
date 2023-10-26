class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.prev, self.curr = self.curr, self.prev + self.curr
        return self.prev
