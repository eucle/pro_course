import pickle
import sys


with open(input(), mode='rb') as pickle_file:
    obj = pickle.load(pickle_file)
    print(obj(*[line.strip('\n') for line in sys.stdin]))
