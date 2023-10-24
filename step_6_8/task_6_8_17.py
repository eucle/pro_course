from collections import Counter


data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.__dict__['max_values'] = lambda: [item for item in data.items()
                                       if item[1] == max(data.values())]
data.__dict__['min_values'] = lambda: [item for item in data.items()
                                       if item[1] == min(data.values())]
