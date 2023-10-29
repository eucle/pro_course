class Alphabet:
    def __init__(self, language):
        if language == 'en':
            self.start = 96
        else:
            self.start = 1071
        self.cnt = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt in {122, 1103}:
            self.cnt = self.start
        self.cnt += 1
        return chr(self.cnt)
