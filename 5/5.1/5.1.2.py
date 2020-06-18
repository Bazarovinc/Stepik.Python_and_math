"""Нахождение производной от e^x"""
from math import exp


def f(x):
    return exp(x)


def def_e(x):
    dx = 0.0001
    return round((f(x + dx) - f(x)) / dx, 3)


print(def_e(1))
print(f(1))
print(def_e(2))
print(f(2))
print(def_e(3))
print(f(3))
print(def_e(4))
print(f(4))
