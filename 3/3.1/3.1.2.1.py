def f(x):
    return x ** 2

x0 = 3
dx_list = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
for dx in dx_list:
    print((f(x0 + dx) - f(x0)) / dx)