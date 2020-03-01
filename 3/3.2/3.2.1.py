import math as m

def f(x):
    return 2 * m.atan(x)

x0 = 1
dx_list = [10, 100, 1000, 10000, 100000, 1000000, 100000000, 10000000000000000]
for dx in dx_list:
    print(f(x0 + dx))
limit = round(f(x0 + dx_list[-1]), 3)
print(limit)