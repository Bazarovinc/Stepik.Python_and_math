def Kfactorial(n, k=1):
    if n == 0 or n <= k:
        return 1
    elif n > k:
        res = 1
        while n >= 1:
            res *= n
            n -= k
        return res
