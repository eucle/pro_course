from collections import Counter


def print_bar_chart(data: str | list, mark: str) -> None:
    res = Counter(data)
    max_len = len(max(res, key=len))
    for k, v in sorted(res.items(), key=lambda x: x[1], reverse=True):
        print(f'{k}{" " * (max_len - len(k))} |{mark * v}')
