class PowerOf:
    def __init__(self, number):
        self.number = number
        self.power = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.power += 1
        return pow(self.number, self.power)
