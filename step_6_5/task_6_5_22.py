from collections import defaultdict


def wins(pairs):
    res_dict = defaultdict(set)
    for winner, loser in pairs:
        res_dict[winner].add(loser)
    return res_dict


result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for losers in result.values():
    print(type(losers) == set)
