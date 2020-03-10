def simple_multiplication(x, y):
    x1 = 100 - x
    y1 = 100 - y
    n = ((100 - (x1 + y1)) * 100) + (x1 * y1)
    return n

print(simple_multiplication(97, 96))
