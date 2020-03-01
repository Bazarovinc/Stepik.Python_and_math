import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 2


def g(x):
    return a * x + b

x0 = 1
dx = 0.0001

a = (f(x0 + dx) - f(x0)) / dx
b = f(x0) - a * x0

x = np.arange(-1, 2, 0.01)
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.show()