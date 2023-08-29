import pickle


def filter_dump(filename, objects, type):
    with open(filename, mode='wb') as f:
        pickle.dump(list(filter(lambda x: isinstance(x, type), objects)), f)


filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
