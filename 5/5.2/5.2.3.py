import math


def derivative(f, x0=0):
    dx = 0.0001
    return round((f(x0 + dx) - f(x0)) / dx, 3)


print(derivative(math.sin))
print(derivative(math.cos))
print(derivative(math.exp, 1))
