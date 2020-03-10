def numerics(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n //= 10
    return nums


def kaprekar_step(L):
    min_1 = sorted(L)
    max_1 = sorted(L, reverse=1)
    n_min = 0
    for i in min_1:
        n_min = n_min * 10 + i
    n_max = 0
    for i in max_1:
        n_max = n_max * 10 + i
    return n_max - n_min


def numerics(n):
    nums = []
    while n > 0:
        nums.append(n % 10)
        n //= 10
    return nums


def kaprekar_check(n):
    L = numerics(n)
    if len(L) < 3 or len(L) == 5 or len(L) > 6:
        return False
    if L.count(L[0]) == len(L):
        return False
    if n == 100 or n == 1000 or n == 100000:
        return False
    return True


def kaprekar_loop(n):
    right_n = [495, 6174, 549945, 631764]
    printed = []
    if kaprekar_check(n):
        print(n)
        printed.append(n)
        while n not in right_n:
            n = kaprekar_step(numerics(n))
            if n not in printed:
                print(n)
                printed.append(n)
            elif n in printed:
                print("Следующее число - " + str(n) + ", кажется процесс зациклился...")
                break
    else:
        print("Ошибка! На вход подано число " + str(n) + ", не удовлетворяющее условиям процесса Капрекара")


kaprekar_loop(76213)