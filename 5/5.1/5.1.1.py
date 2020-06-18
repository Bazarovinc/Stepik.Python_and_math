from math import atan


"""Предел функции 2 * arctg(x) при х стремящемся к бесконечности"""


def f(x):
    return 2 * atan(x)


x1 = 1e6
x2 = 1e7
x3 = 1e10
print(f(x1))
print(f(x2))
print(f(x3))
print(round(f(x1), 3), round(f(x2), 3), round(f(x3), 3))
