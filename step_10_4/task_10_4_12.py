class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.lst = list(data)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.lst):
            raise StopIteration
        return self.lst[self.index], self.data[self.lst[self.index]]
