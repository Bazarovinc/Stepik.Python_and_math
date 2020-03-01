def dfactorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                res *= i
        elif n % 2 != 0:
            for i in range(1, n + 1, 2):
                res *= i
        return res
