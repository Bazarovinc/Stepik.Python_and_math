def wisdom_multiplication(x, y, length_check = True):
    x1 = 100 - x
    y1 = 100 - y
    step_2 = x1 + y1
    step_3 = 100 - step_2
    step_4 = x1 * y1
    if step_3 > 0:
        step_3 = str(step_3)
        step_4 = str(step_4)
        if length_check:
            if len(step_4) == 1:
                step_3 += '0'
    else:
        if length_check:
            if step_4 <= 9:
                step_3 *= 100
            else:
                step_3 *= 10
        else:
           step_3 *= 10
    res = step_3 + step_4
    return int(res)


def multiplication_check_list(start=10, stop=99, length_check = True):
    if start < stop:
        n1, n2 = start, stop
    else:
        n1, n2 = start, stop
        start, stop = stop, start
    true_res = 0
    false_res = 0
    for i in range(n1, n2 + 1):
        for j in range(n1, n2 + 1):
            if wisdom_multiplication(i, j, length_check) == i * j:
                true_res += 1
            else:
                false_res += 1
    print("Правильных результатов:", true_res)
    print("Неправильных результатов:", false_res)
    print(true_res + false_res)


multiplication_check_list(length_check=False)
