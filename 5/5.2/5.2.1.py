def f(x):
    return (2 * pow(x, 2) - 3 * x - 5) / (3* pow(x, 2) + x + 1)


print(round(f(1e10), 3))
print(round(f(-1e10), 3))
