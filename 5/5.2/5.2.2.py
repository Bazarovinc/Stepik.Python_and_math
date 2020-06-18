import numpy as np


def f(x):
    return (np.sin((np.pi * x) / 2)) / x


print(round(f(5e10), 3))
