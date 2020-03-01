from math import exp

def f(x):
    return (exp(x) - 1) / x

x0 = 0
dx_list = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
for dx in dx_list:
    print(f(x0 + dx))