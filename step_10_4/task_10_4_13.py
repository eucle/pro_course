class CardDeck:
    def __init__(self):
        self.suit = ("пик", "треф", "бубен", "червей")
        self.rank = [*[i for i in range(2, 11)],
                     "валет", "дама", "король", "туз"]
        self.suit_idx = 0
        self.rank_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.suit_idx > 3:
            raise StopIteration
        card = f"{self.rank[self.rank_idx]} {self.suit[self.suit_idx]}"
        self.rank_idx += 1
        if self.rank_idx > 12:
            self.rank_idx = 0
            self.suit_idx += 1
        return card
