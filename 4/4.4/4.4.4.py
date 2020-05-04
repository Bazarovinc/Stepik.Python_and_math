def wisdom_multiplication(x, y, length_check = True):
    x1 = 100 - x
    y1 = 100 - y
    step_2 = x1 + y1
    step_3 = 100 - step_2
    step_4 = x1 * y1
    step_3 = str(step_3)
    step_4 = str(step_4)
    if length_check:
        if len(step_4) == 1:
            step_3 += '0'
    res = step_3 + step_4
    return int(res)


print(wisdom_multiplication(99, 99))