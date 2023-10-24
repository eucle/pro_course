user_collection = eval(input())
if type(user_collection) == list:
    print(user_collection[-1])
elif type(user_collection) == tuple:
    print(user_collection[0])
else:
    print(len(user_collection))
