from collections import OrderedDict


data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да',
                    'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ',
                    'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2',
                    'SeatsCount': '10'})

new_data, last = OrderedDict(), False
for key in list(data):
    key, value = data.popitem(last=last)
    new_data[key] = value
    last = not last

print(new_data)
