from calendar import monthrange


print(monthrange(*map(int, input().split()))[1])
