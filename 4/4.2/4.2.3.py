def L(n):
    luka = [2, 1, 3, 4, 7, 11, 18, 29]
    if len(luka) - 1 >= n:
        return luka[n]
    else:
        i = len(luka) - 1
        luka = luka[-2:]
        while i != n:
            luka.append(luka[-1] + luka[-2])
            luka = luka[-2:]
            i += 1
        return luka[-1]


def L2(n):
    n1 = L(n)
    res = ((n1 ** 2) - 2 * pow(-1, n))
    return res


def L4(n):
    n1 = L(n)
    res = (pow(n1, 4) - 4 * pow(-1, n) * pow(n1, 2) + 2)
    return res


def super_L(n):
    if n % 4 == 0:
        return L4(n // 4)
    if n % 2 == 0:
        return L2(n // 2)
    else:
        return L(n)


print(super_L(3 ** 10))
#print(L2(8))
