from collections import defaultdict


def flip_dict(dict_of_lists):
    res_dict = defaultdict(list)
    for key, values in dict_of_lists.items():
        for value in values:
            res_dict[value].append(key)
    return res_dict


data = {'Arthur': ['cacao', 'tea', 'juice'],
        'Timur': ['coffee', 'tea', 'juice'],
        'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')
