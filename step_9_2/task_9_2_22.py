fn = input()
a, b = input().split()
mini = min([eval(fn) for x in range(int(a), int(b) + 1)])
maxi = max([eval(fn) for x in range(int(a), int(b) + 1)])
print(f'Минимальное значение функции {fn} на отрезке [{a}; {b}] равно {mini}')
print(f'Максимальное значение функции {fn} на отрезке [{a}; {b}] равно {maxi}')