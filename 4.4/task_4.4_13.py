import json

pools = []
with open('pools.json', 'r', encoding='utf-8') as j_file:
    for pool in json.load(j_file):
        if (int(pool['WorkingHoursSummer']['Понедельник'][:2]) <= 10
           and int(pool['WorkingHoursSummer']['Понедельник'][6:8]) >= 12):
            pools.append(pool)

spec_pool = max(pools, key=lambda x: (x['DimensionsSummer']['Length'],
                                      x['DimensionsSummer']['Width']))
print(f"{spec_pool['DimensionsSummer']['Length']}x{spec_pool['DimensionsSummer']['Width']}")
print(f"{spec_pool['Address']}")
