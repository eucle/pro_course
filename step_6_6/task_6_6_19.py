from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    for key in sorted(ordered_dict.items(), key=lambda x: x[by_values]):
        ordered_dict.move_to_end(key[0])


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)

print(data)
