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


def kaprekar_loop(n):
    if n > 1000:
        print(n)
        while n != 6174:
                n = kaprekar_step(numerics(n))
                print(n)


kaprekar_loop(8333)
