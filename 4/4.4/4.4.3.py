def simple_multiplication(x, y):
    x1 = 100 - x
    y1 = 100 - y
    n = ((100 - (x1 + y1)) * 100) + (x1 * y1)
    return n


def multiplication_check(x, y):
    if x * y == simple_multiplication(x, y):
        return True
    return False


def multiplication_check_list(start=10, stop=99):
    right = 0
    wrong = 0
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            if multiplication_check(i, j):
                right += 1
            else:
                wrong += 1
    print("Правильных результатов: ", right)
    print("Неправильных результатов: ", wrong)


multiplication_check_list()
