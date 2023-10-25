class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1
        if self.cnt <= self.times:
            return self.obj
        else:
            raise StopIteration
