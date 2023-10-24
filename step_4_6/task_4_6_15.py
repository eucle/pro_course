import pickle


ans = ['Контрольные суммы не совпадают', 'Контрольные суммы совпадают']

with open(input(), mode='rb') as file:
    control_sum = int(input())
    obj = pickle.load(file)
    if type(obj) == list:
        int_list = list(filter(lambda x: isinstance(x, int), obj))
        print(ans[max(int_list, default=0) *
                  min(int_list, default=0) == control_sum])
    else:
        int_sum = sum(filter(lambda x: type(x) == int, obj.keys()))
        print(ans[int_sum == control_sum])
