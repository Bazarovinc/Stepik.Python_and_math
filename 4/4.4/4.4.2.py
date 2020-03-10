def simple_multiplication(x, y):
    x1 = 100 - x
    y1 = 100 - y
    n = ((100 - (x1 + y1)) * 100) + (x1 * y1)
    return n

def multiplication_check(x, y):
    if x * y == simple_multiplication(x, y):
        return True
    return False

print(multiplication_check(97, 96))
