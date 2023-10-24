from collections import Counter


def scrabble(symbols: str, word: str) -> bool:
    return Counter(symbols.lower()) >= Counter(word.lower())
